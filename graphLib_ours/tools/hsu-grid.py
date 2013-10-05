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
from igraph import Graph

def usage():
    'print usage'
    print 'usage: %s [options]' % sys.argv[0]


def grid(p, q):
    g = Graph(p * q)
    g.vs["label"] = [str(x) for x in range(1, p*q+1)]

    def v2i(i, j):
        return i * q + j
    def i2v(i):
        return (i / q, i % q)

    for i in range(p - 1):
        for j in range(q):
            # vertical
            edge = (v2i(i, j), v2i(i + 1, j))
            g.add_edges(edge)

    for i in range(p):
        for j in range(q - 1):
            # horizontal
            for i_ in range(i, p):
                edge = (v2i(i, j), v2i(i_, j + 1))
                g.add_edges(edge)
    return g

def dimacs(g):
    s = []
    def o(x):
        s.append(x)
    o('p edges %d %d' % (len(g.vs), len(g.es)))
    tuples = [e.tuple for e in g.es]
    tuples.sort()
    for x, y in tuples:
        x += 1
        y += 1
        o('e %d %d' % (x, y))
    return '\n'.join(s)

def main():
    'entry point'
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    if len(sys.argv) == 2:
        p = q = int(sys.argv[1])
    else:
        p = int(sys.argv[1])
        q = int(sys.argv[2])

    g = grid(p, q)
    fname = 'hsu-%dx%d.dimacs' % (p, q)
    fd = file(fname, 'w')
    fd.write(dimacs(g))
    fd.close()

    fname = 'hsu-%dx%d.dot' % (p, q)
    g.write_dot(fname)

    fname = 'hsu-%dx%d.gml' % (p, q)
    g.write_gml(fname)


if __name__ == '__main__':
    main()

