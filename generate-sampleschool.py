#!/usr/bin/env python
"""
A script to generate sample school data.
"""

import sys
if sys.version_info < (2, 3):
    print >> sys.stderr, '%s: need Python 2.3 or later.' % sys.argv[0]
    print >> sys.stderr, 'Your python is %s' % sys.version
    sys.exit(1)

import os
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(basedir, 'src'))

import schooltool.clients.datagen
schooltool.clients.datagen.main(['datagen', 'schooltool-m4'])