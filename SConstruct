# -*- coding: utf-8 -*-

import util.build_util as build_util
import util.build_config as build_config

build_util.info_print()

env = Environment(
    CFLAGS=build_config.cflags,
    CPPPATH=build_config.includes,
    )

prog = env.Program(
    'neoagent',
    [ Glob('*.c'), Glob('ext/*.c') ],
    LIBS=build_config.libs,
    )

if 'configure' in COMMAND_LINE_TARGETS:
    if build_util.configure(Configure(env), build_config.libs) is False:
        Exit(1)
    else:
        Exit(0)
elif 'install' in COMMAND_LINE_TARGETS:
    build_util.install(env, prog, ARGUMENTS.get('prefix', '/usr/local/'))
elif 'debian' in COMMAND_LINE_TARGETS:
    SConscript("debian/SConscript")
elif 'doc' in COMMAND_LINE_TARGETS:
    SConscript("doc/SConscript")
