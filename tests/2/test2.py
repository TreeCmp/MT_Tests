#!/usr/bin/env python

import sys
import subprocess
import os

treeCmpApp = "../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar"
testTreesPath = "shrink_trees"
outFilePath = "m3_res"


def ComputeM3distances(treeCmpApp, testTreesPath, outFilePath):
    for (dirpath, dirnames, filenames) in os.walk(testTreesPath):
        for filename in filenames:  
            subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", testTreesPath + "/" + filename, "-o", outFilePath + "/" + filename + ".out"])

ComputeM3distances(treeCmpApp, testTreesPath, outFilePath)
