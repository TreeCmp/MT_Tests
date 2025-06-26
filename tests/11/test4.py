#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

unrooted = '-u'
binary = '-b'
arbitrary = '-a'

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

treesPath_n9 = 'catep_n_9.newick'
resPath_n9 = 'catep_n_9.out'
treesPath_n12 = 'catep_n_12.newick'
resPath_n12 = 'catep_n_12.out'

# dMT (T1, T2) = n(n−3)/2
#for n=9 distance should be 9(9−3)/2 = 27
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", treesPath_n9, "-o", resPath_n9])
#for n=12 distance should be 12(12−3)/2 = 54
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", treesPath_n12, "-o", resPath_n12])

