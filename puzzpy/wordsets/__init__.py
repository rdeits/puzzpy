import os
import puzzpy


def load_wordlist(wordlist):
    fname = os.path.join(puzzpy.root_path(), 'data', 'dictionaries', wordlist)
    if not os.path.exists(fname):
        fname += '.txt'
    with open(fname) as f:
        entries = f.read().split('\n')
    for i, e in enumerate(entries):
        if e.startswith('--'):
            break
    return set(puzzpy.phrase_cleanup(e) for e in entries[i+1:])
