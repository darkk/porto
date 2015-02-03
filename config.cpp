#include <iostream>

#include "config.hpp"
#include "util/protobuf.hpp"
#include "util/unix.hpp"

extern "C" {
#include <fcntl.h>
#include <unistd.h>
}

using std::string;

TConfig config;

void TConfig::LoadDefaults() {
    config().mutable_network()->set_enabled(true);
    config().mutable_network()->set_debug(false);
    config().mutable_network()->set_default_prio(3);
    config().mutable_network()->set_default_max_guarantee(-1);
    config().mutable_network()->set_default_guarantee(-1);
    config().mutable_network()->set_default_limit(-1);
    config().mutable_network()->set_dynamic_ifaces(false);

    config().mutable_slave_pid()->set_path("/run/portod.pid");
    config().mutable_slave_pid()->set_perm(0644);
    config().mutable_slave_log()->set_path("/var/log/portod.log");
    config().mutable_slave_log()->set_perm(0644);

    config().mutable_master_pid()->set_path("/run/portoloop.pid");
    config().mutable_master_pid()->set_perm(0644);
    config().mutable_master_log()->set_path("/var/log/portoloop.log");
    config().mutable_master_log()->set_perm(0644);

    config().mutable_rpc_sock()->mutable_file()->set_path("/run/portod.socket");
    config().mutable_rpc_sock()->mutable_file()->set_perm(0660);
    config().mutable_rpc_sock()->set_group("porto");

    config().mutable_log()->set_verbose(false);

    config().mutable_keyval()->mutable_file()->set_path("/run/porto/kvs");
    config().mutable_keyval()->mutable_file()->set_perm(0755);
    config().mutable_keyval()->set_size("size=32m");

    config().mutable_daemon()->set_max_clients(128);
    config().mutable_daemon()->set_slave_read_timeout_s(5);
    config().mutable_daemon()->set_cgroup_remove_timeout_s(1);
    config().mutable_daemon()->set_freezer_wait_timeout_s(2);
    config().mutable_daemon()->set_memory_guarantee_reserve(2 * 1024 * 1024 * 1024UL);
    config().mutable_daemon()->mutable_pidmap()->set_path("/tmp/portod.pidmap");
    config().mutable_daemon()->set_rotate_logs_timeout_s(60);
    config().mutable_daemon()->set_sysfs_root("/sys/fs/cgroup");
    config().mutable_daemon()->set_batch_sync(false);

    config().mutable_container()->set_max_log_size(10 * 1024 * 1024);
    config().mutable_container()->set_tmp_dir("/place/porto");
    config().mutable_container()->set_aging_time_s(60 * 60 * 24 * 7);
    config().mutable_container()->set_respawn_delay_ms(1000);
    config().mutable_container()->set_stdout_limit(8 * 1024 * 1024);
    config().mutable_container()->set_private_max(1024);
    config().mutable_container()->set_default_cpu_prio(50);
    config().mutable_container()->set_kill_timeout_ms(1000);
    config().mutable_container()->set_stop_timeout_ms(1000);
    config().mutable_container()->set_use_hierarchy(true);
    config().mutable_container()->set_max_total(3000);

    config().mutable_volumes()->mutable_keyval()->mutable_file()->set_path("/run/porto/pkvs");
    config().mutable_volumes()->mutable_keyval()->mutable_file()->set_perm(0755);
    config().mutable_volumes()->mutable_keyval()->set_size("size=32m");

    config().mutable_volumes()->set_volume_dir("/place/porto_volumes");
    config().mutable_volumes()->set_resource_dir("/place/porto_resources");
    // TODO: make sure we pick up correct default here depending on kernel
    // version
    config().mutable_volumes()->set_native(false);
}

bool TConfig::LoadFile(const std::string &path, bool silent) {
    TScopedFd fd(open(path.c_str(), O_RDONLY | O_CLOEXEC));
    if (fd.GetFd() < 0)
        return false;

    google::protobuf::io::FileInputStream pist(fd.GetFd());

    if (!google::protobuf::TextFormat::Merge(&pist, &Cfg) ||
        !Cfg.IsInitialized()) {
        return false;
    }

    if (!silent)
        std::cerr << "Using config " << path << std::endl;

    return true;
}

void TConfig::Load(bool silent) {
    LoadDefaults();

    for (auto &path : ConfigFiles)
        if (LoadFile(path, silent))
            goto load_cred;

    if (!silent)
        std::cerr << "Using default config" << std::endl;

    if (config().container().aging_time_s() <
        config().daemon().rotate_logs_timeout_s()) {
        std::cerr << "aging_time_s should be greater than rotate_logs_timeout_s" << std::endl;
        throw string("Invalid configuration");
    }

load_cred:
    CredConf.Load();
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
