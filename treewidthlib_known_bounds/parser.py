#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re
from BeautifulSoup import BeautifulSoup

def parse(fname):
    html = file(fname).read()
    soup = BeautifulSoup(html)

    rows = soup.findAll('tr')

    for row in rows:
        match = 'graph.php' in str(row)
        if not match:
            continue
        baseurl = 'http://people.cs.uu.nl/hansb/treewidthlib/'
        url = baseurl + row.findAll('a')[0].get('href')
        url = url.strip()
        contents = [x.contents[0] for x in row.findAll('a')]
        try:
            graph, measure, lbound, ubound = contents
        except:
            print 'ignoring', contents
            continue
        lbound = int(lbound)
        ubound = int(ubound)
        print url, graph, measure, lbound, ubound

def usage():
    'print usage'
    print 'usage: %s [options]' % sys.argv[0]

def main():
    'entry point'
    if len(sys.argv) < 1:
        usage()
        sys.exit(1)

    fnames = sys.argv[1:]
    for fname in fnames:
        parse(fname)

if __name__ == '__main__':
    main()

