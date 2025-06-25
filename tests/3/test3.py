#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

unrooted = '-u'
binary = '-b'
arbitrary = '-a'

treeCmpApp = "../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar"
ptrGenAppName = "PRTGen.exe"
genTreesFileDir = "all_trees"
genTreesResFileDir = "all_trees_res"
curDir = os.path.dirname(os.path.abspath(__file__))
mainDir = Path(curDir).parents[1]
softPath = mainDir / "soft"
prtGenDir = softPath / "PRTGen"
prtGenPath = prtGenDir / ptrGenAppName

genTreesFilePath = Path(curDir, genTreesFileDir)
genTreesResFilePath = Path(curDir, genTreesResFileDir)


if not genTreesFilePath.exists():
    os.makedirs(genTreesFilePath)
if not genTreesResFilePath.exists():
    os.makedirs(genTreesResFilePath)
for n in range(5, 9):

        binaryTreesPath = Path(genTreesFilePath, "all_b_n_" + str(n) + "_trees.newick")
        binaryTreesResultPath = Path(genTreesResFilePath, "all_b_n_" + str(n) + "_trees.out")
        print (subprocess.list2cmdline([prtGenPath, "-n", str(n), unrooted, binary, "-f", binaryTreesPath]))
        subprocess.check_call([prtGenPath, "-n", str(n), unrooted, binary, "-f", binaryTreesPath])
        print (subprocess.list2cmdline(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", binaryTreesPath, "-o", binaryTreesResultPath]))
        subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", binaryTreesPath, "-o", binaryTreesResultPath])

        # arbitraryTreesPath = Path(genTreesFilePath, "all_a_n_" + str(n) + "_trees.newick")
        # print (subprocess.list2cmdline([prtGenPath, "-n", str(n), unrooted, arbitrary, "-f", arbitraryTreesPath]))
        # subprocess.check_call([prtGenPath, "-n", str(n), unrooted, arbitrary, "-f", arbitraryTreesPath])