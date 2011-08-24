# -*- coding: utf-8 -*-

import sys
import SCons

def info_print():
    print "Python " + ".".join([ str(i) for i in sys.version_info ])
    print "SCons  " + SCons.__version__

def configure(conf, libs):
    if not conf.CheckCXX():
        print "c++ compiler is not installed!"
        return False

    for lib in libs:
        if not conf.CheckLib(lib):
            print "library " + lib + " not installed!"
            return False
    conf.Finish()
    return True

def install(env, prog, prefix):
    bin_dir = prefix + 'bin/'
    man_dir = prefix + 'share/man/man1/'
    env.Alias(target="install", source=env.Install(bin_dir, prog))
    env.Install(bin_dir, prog)
    env.Alias(target="install", source=env.Install(man_dir, 'doc/build/man/neoagent.1'))
    env.Install(man_dir, 'doc/build/man/neoagent.1')

