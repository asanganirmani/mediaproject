#!/usr/bin/env python
"""
A script to start the schooltool client from the source directory.
"""

import sys
if sys.version_info < (2, 3):
    print >> sys.stderr, '%s: need Python 2.3 or later.' % sys.argv[0]
    print >> sys.stderr, 'Your python is %s' % sys.version
    sys.exit(1)

import os
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(basedir, 'src'))

import schooltool.clients.client
schooltool.clients.client.main()
