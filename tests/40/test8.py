#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

# UT_1A,UT_2A unrooted (n=20)
#(((17,(5,((16,12),(9,8)))),(18,(7,1))),(13,(4,(3,11))),((19,2),(15,(14,(10,(6,20))))));
#(((13,(20,((5,(7,12)),(19,2)))),(15,(6,17))),(1,9),(((14,(18,3)),(10,4)),(16,(8,11))));
unrooted_trees_u_n20_Path = 'tress_n_u_20.newick'
unrooted_trees_u_n20_PathRes = 'trees_n_u_20.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_u_n20_Path, "-o", unrooted_trees_u_n20_PathRes])
#qt(UT_1A,UT_2A) = 3231

# UT_1B,UT_2B unrooted (n=11)
#(28,((26,(30,(22,(29,25)))),(31,(27,21))),(23,24));
#((24,((26,27),(22,21))),((29,25),(30,31)),(23,28));
unrooted_trees_u_n11_Path = 'tress_n_u_11.newick'
unrooted_trees_u_n11_PathRes = 'trees_n_u_11.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_u_n11_Path, "-o", unrooted_trees_u_n11_PathRes])
#qt(UT_1B,UT_2B) = 198

# T_1A,T_2A rooted (n=20)
#((((17,(5,((16,12),(9,8)))),(18,(7,1))),(13,(4,(3,11)))),((19,2),(15,(14,(10,(6,20))))));
#((((13,(20,((5,(7,12)),(19,2)))),(15,(6,17))),(1,9)),(((14,(18,3)),(10,4)),(16,(8,11))));
rooted_trees_u_n20_Path = 'tress_n_20.newick'
rooted_trees_u_n20_PathRes = 'trees_n_20.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "rf", "-i", rooted_trees_u_n20_Path, "-o", rooted_trees_u_n20_PathRes])
#rf(T_1A,T_2A) = 16

# T_1B,T_2B rooted (n=11)
#(28,(((26,(30,(22,(29,25)))),(31,(27,21))),(23,24)));
#(((24,((26,27),(22,21))),((29,25),(30,31))),(23,28));
rooted_trees_u_n11_Path = 'tress_n_11.newick'
rooted_trees_u_n11_PathRes = 'trees_n_11.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "rf", "-i", rooted_trees_u_n11_Path, "-o", rooted_trees_u_n11_PathRes])
#rf(T_1A,T_2A) = 7

# 3231 + 198 + 11 * 16 + 20 * 7 = 3745

#((28,(((26,(30,(22,(29,25)))),(31,(27,21))),(23,24))),(((17,(5,((16,12),(9,8)))),(18,(7,1))),(13,(4,(3,11)))),((19,2),(15,(14,(10,(6,20))))));
#((((24,((26,27),(22,21))),((29,25),(30,31))),(23,28)),(((13,(20,((5,(7,12)),(19,2)))),(15,(6,17))),(1,9)),(((14,(18,3)),(10,4)),(16,(8,11))));

unrooted_trees_u_n31_Path = 'tress_n_31.newick'
unrooted_trees_u_n31_PathRes = 'trees_n_31.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_u_n31_Path, "-o", unrooted_trees_u_n31_PathRes])
#qt(T_1A-T_1B,T_2A-T_2B) = 13438