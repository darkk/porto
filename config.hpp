#ifndef __CONFIG_H__
#define __CONFIG_H__

#include <string>

#include "config.pb.h"

/*
/etc/portod.conf
/etc/default/portod.conf
*/

class TConfig {
    cfg::TCfg Cfg;

    void LoadDefaults();
    bool LoadFile(const std::string &path);
public:
    void Load();
    cfg::TCfg &operator()();
};

extern TConfig config;

#endif