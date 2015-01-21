from __future__ import print_function, division

# from bs4 import BeautifulSoup
# import subprocess
# import tempfile
import os
import wikipedia
import re

import puzzpy


def wiki_cleanup(phrase):
    return re.sub(r'\([^\)]*\)', '', phrase)


def get_list(title):
    fname = puzzpy.file_cleanup(os.path.join(puzzpy.root_path(),
                         'data', 'wiki', title))
    if not os.path.exists(fname):
        page = wikipedia.page(title)
        entries = [puzzpy.phrase_cleanup(wiki_cleanup(e)) for e in page.links]

        with open(fname, 'w') as f:
            f.write('\n'.join(sorted(set(entries))))
    else:
        with open(fname) as f:
            entries = f.read().split('\n')
    return set(entries)


    # if '/' in title_or_url:
    #     url = title_or_url
    #     title = title_or_url.split('/')[-1]
    # else:
    #     title = title_or_url
    #     url = "http://en.wikipedia.org/wiki/" + title.replace(' ', '_')
    # fname = puzzpy.file_cleanup(os.path.join(puzzpy.root_path(),
    #                      'data', 'wiki', title))
    # if not os.path.exists(fname):
    #     fid, temp_fname = tempfile.mkstemp()
    #     if not os.path.exists(os.path.dirname(fname)):
    #         os.makedirs(os.path.dirname(fname))
    #     subprocess.call(['wget', url, '-O', temp_fname])
    #     # subprocess.call(['cp', 'List_of_common_fish_names', temp_fname])
    #     with open(temp_fname) as f:
    #         soup = BeautifulSoup(f)
    #     content = soup.find(id='mw-content-text')
    #     entries = []
    #     # for div in content.find_all('div', class_='div-col'):
    #     for link in content.find_all('a'):
    #         if link.get('href').startswith('/wiki/'):
    #             entry = puzzpy.phrase_cleanup(link.get_text())
    #             if entry:
    #                 entries.append(entry)
    #     with open(fname, 'w') as f:
    #         f.write('\n'.join(sorted(set(entries))))
    # else:
    #     with open(fname) as f:
    #         entries = f.read().split('\n')
    # return set(entries)
