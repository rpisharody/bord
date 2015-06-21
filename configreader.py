#!/usr/bin/env python3
'''
    Config File reader for bord.

    Parses the config file as argument and returns a dictionary
    with the parsed values.
'''

import os
import configparser


def ConfigReader(filename):
    filename = os.path.expanduser(filename)
    config = configparser.ConfigParser()
    try:
        with open(filename, 'r') as f:
            config.read_file(f, filename)
    except IOError as e:
        print ('Error :', e.strerror)

    opt_dict = {}
    for sec in config.sections():
        for opt in config.options(sec):
            opt_dict[opt] = config[sec][opt]

    # Expand file and directory names to full path
    expand_list = ('output_dir', 'content_dir')
    # Supports usage of ENV variables in config file.
    # Expands 'working_dir' to get rid of relpaths and envs
    opt_dict['working_dir'] = os.path.realpath(
        os.path.expandvars(opt_dict['working_dir'])
    )
    for element in expand_list:
        opt_dict[element] = os.path.join(
            opt_dict['working_dir'],
            opt_dict[element]
        )

    return opt_dict

# TODO:
# 1. Putting defaults for missing config params
# 2. Logging/Error ?
