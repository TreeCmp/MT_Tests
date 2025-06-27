#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

# T_1,T_2 rooted (n=16)
#(((((10,(15,9)),(4,16)),(8,(6,(3,(2,5))))),(7,(1,(14,13)))),(12,11));
#(16,(((13,((14,(3,8)),(4,9))),(5,(7,10))),((12,1),(2,(11,(15,6))))));
rooted_trees_n16_Path = 'tress_n_16.newick'
rooted_trees_n16_PathRes = 'trees_n_16.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "tt", "-i", rooted_trees_n16_Path, "-o", rooted_trees_n16_PathRes])
#d_tt(T_1,T_2) = 379

# U(T_1),U(T_2) unrooted (n=16)
#(((((10,(15,9)),(4,16)),(8,(6,(3,(2,5))))),(7,(1,(14,13)))),12,11);
#(16,((13,((14,(3,8)),(4,9))),(5,(7,10))),((12,1),(2,(11,(15,6)))));
unrooted_trees_n16_Path = 'tress_u_n_16.newick'
unrooted_trees_n16_PathRes = 'trees_u_n_16.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_n16_Path, "-o", unrooted_trees_n16_PathRes])
#d_qt(U(T_1),U(T_2)) = 1294

# T_1K_1,B,T_2K_1,B dla B=(17,18,19,20);
#(((((10,(15,9)),(4,16)),(8,(6,(3,(2,5))))),(7,(1,(14,13)))),(12,11),(17,18,19,20));
#(16,(((13,((14,(3,8)),(4,9))),(5,(7,10))),((12,1),(2,(11,(15,6))))),(17,18,19,20));
unrooted_trees_K1B_n20_Path = 'tress_n_20.newick'
unrooted_trees_K1B_n20_PathRes = 'trees_n_20.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_K1B_n20_Path, "-o", unrooted_trees_K1B_n20_PathRes])
#d_qt(T_1K_1,B,T_2K_1,B) = 3044

# 2810 = 4 * 379 + 1294