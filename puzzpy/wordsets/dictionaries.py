from __future__ import print_function, division

import os

import puzzpy


def sowpods():
    with open(os.path.join(puzzpy.root_path(), 'data', 'dictionaries', 'sowpods.txt')) as f:
        entries = f.read().split('\n')
    assert entries[0] == 'aa', 'please remove any header fromt the sowpods.txt file'
    sowpods = set(entries)
    return sowpods


def ukacd():
    with open(os.path.join(puzzpy.root_path(), 'data', 'dictionaries', 'UKACD.txt')) as f:
        entries = f.read().split('\n')
    for i, e in enumerate(entries):
        if e.startswith('-'):
            break
    ukacd = set(puzzpy.phrase_cleanup(e) for e in entries[i+1:])
    return ukacd
