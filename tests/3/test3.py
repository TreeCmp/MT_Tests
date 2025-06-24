#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

unrooted = 'u'

ptrGenAppName = "PRTGen.exe"
genTreesFileDir = "all_trees"
curDir = os.path.dirname(os.path.abspath(__file__))
mainDir = Path(curDir).parents[1]
softPath = mainDir / "soft"
prtGenDir = softPath / "PRTGen"
prtGenPath = prtGenDir / ptrGenAppName

genTreesFilePath = Path(curDir, genTreesFileDir)



if not genTreesFilePath.exists():
    os.makedirs(genTreesFilePath)
for n in range(6, 9):

        treesPath = Path(genTreesFilePath, "all_n_" + str(n) + "_trees.newick")
        print (subprocess.list2cmdline([prtGenPath, "-n", str(n), "-" + unrooted, "-f", treesPath]))
        subprocess.check_call([prtGenPath, "-n", str(n), "-" + unrooted, "-f", treesPath])