#include <iostream>

#include "config.hpp"
#include "protobuf.hpp"
#include "util/unix.hpp"
#include "util/mount.hpp"
#include "util/log.hpp"

extern "C" {
#include <fcntl.h>
#include <unistd.h>
}

using std::string;

TConfig config;

void TConfig::LoadDefaults() {
    config().mutable_slave_pid()->set_path("/run/portod.pid");
    config().mutable_slave_pid()->set_perm(0644);
    config().mutable_slave_log()->set_path("/var/log/portod.log");
    config().mutable_slave_log()->set_perm(0644);

    config().mutable_master_pid()->set_path("/run/portoloop.pid");
    config().mutable_master_pid()->set_perm(0644);
    config().mutable_master_log()->set_path("/var/log/portoloop.log");
    config().mutable_master_log()->set_perm(0644);

    config().mutable_log()->set_verbose(false);

    config().mutable_keyval()->mutable_file()->set_path("/run/porto/kvs");
    config().mutable_keyval()->mutable_file()->set_perm(0755);
    config().mutable_keyval()->set_size("size=32m");

    config().mutable_daemon()->set_max_clients(512);
    config().mutable_daemon()->set_cgroup_remove_timeout_s(5);
    config().mutable_daemon()->set_freezer_wait_timeout_s(5 * 60);
    config().mutable_daemon()->set_memory_guarantee_reserve(2 * 1024 * 1024 * 1024UL);
    config().mutable_daemon()->set_rotate_logs_timeout_s(60);
    config().mutable_daemon()->set_sysfs_root("/sys/fs/cgroup");
    config().mutable_daemon()->set_memory_limit(1 * 1024 * 1024 * 1024);
    config().mutable_daemon()->set_workers(4);
    config().mutable_daemon()->set_max_msg_len(32 * 1024 * 1024);
    config().mutable_daemon()->set_event_workers(1);

    config().mutable_container()->set_max_log_size(10 * 1024 * 1024);
    config().mutable_container()->set_tmp_dir("/place/porto");
    config().mutable_container()->set_chroot_porto_dir("porto");
    config().mutable_container()->set_default_aging_time_s(60 * 60 * 24);
    config().mutable_container()->set_respawn_delay_ms(1000);
    config().mutable_container()->set_stdout_limit(8 * 1024 * 1024);
    config().mutable_container()->set_private_max(1024);
    config().mutable_container()->set_kill_timeout_ms(1000);
    // wait 30 seconds for container process to exit after SIGKILL
    config().mutable_container()->set_stop_timeout_ms(30 * 1000);
    config().mutable_container()->set_max_total(3000);
    config().mutable_container()->set_batch_io_weight(10);
    config().mutable_container()->set_empty_wait_timeout_ms(5000);

    config().mutable_volumes()->mutable_keyval()->mutable_file()->set_path("/run/porto/pkvs");
    config().mutable_volumes()->mutable_keyval()->mutable_file()->set_perm(0755);
    config().mutable_volumes()->mutable_keyval()->set_size("size=32m");

    config().mutable_volumes()->set_volume_dir("/place/porto_volumes");
    config().mutable_volumes()->set_layers_dir("/place/porto_layers");
    config().mutable_volumes()->set_enable_quota(true);

    config().mutable_network()->set_autoconf_timeout_s(120);
}

bool TConfig::LoadFile(const std::string &path) {
    TScopedFd fd(open(path.c_str(), O_RDONLY | O_CLOEXEC));
    if (fd.GetFd() < 0)
        return false;

    google::protobuf::io::FileInputStream pist(fd.GetFd());

    if (!google::protobuf::TextFormat::Merge(&pist, &Cfg) ||
        !Cfg.IsInitialized()) {
        return false;
    }

    return true;
}

void TConfig::Load() {
    LoadDefaults();

    for (auto &path : ConfigFiles)
        if (LoadFile(path))
            goto load_cred;

    if (config().container().default_aging_time_s() <
        config().daemon().rotate_logs_timeout_s()) {
        std::cerr << "default_aging_time_s should be greater than rotate_logs_timeout_s" << std::endl;
        throw string("Invalid configuration");
    }

load_cred:
    Verbose = config().log().verbose();

    InitCred();
}

int TConfig::Test(const std::string &path) {
    if (access(path.c_str(), F_OK)) {
        std::cerr << "Config " << path << " doesn't exist" << std::endl;
        return EXIT_FAILURE;
    }

    TScopedFd fd(open(path.c_str(), O_RDONLY | O_CLOEXEC));
    if (fd.GetFd() < 0) {
        std::cerr << "Can't open " << path << std::endl;
        return EXIT_FAILURE;
    }

    google::protobuf::io::FileInputStream pist(fd.GetFd());

    cfg::TCfg cfg;
    if (!google::protobuf::TextFormat::Merge(&pist, &cfg))
        return EXIT_FAILURE;

    return EXIT_SUCCESS;
}

cfg::TCfg &TConfig::operator()() {
    return Cfg;
}
