#!/usr/bin/env python

import sys
import subprocess
import os

treeCmpApp = "../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar"
testBinTreesPath = "nni_trees"
outFileBinPath = "m3_res"
outFileArbPath = "nni_arb_trees"
testArbTreesPath = "m3_arb_res"


def ComputeM3distances(treeCmpApp, testTreesPath, outFilePath):
    for (dirpath, dirnames, filenames) in os.walk(testTreesPath):
        for filename in filenames:  
            subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", testTreesPath + "/" + filename, "-o", outFilePath + "/" + filename + ".out"])

# ComputeM3distances(treeCmpApp, testBinTreesPath, outFileBinPath)

ComputeM3distances(treeCmpApp, outFileArbPath, testArbTreesPath)
