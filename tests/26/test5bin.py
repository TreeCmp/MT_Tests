#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

# T_1,T_2 unrooted (n=17)
#(((('1','2'),('3','4')),((('5','6'),'7'),'8')),((('9','10'),'11'),('12','13')),('14',('15',('16','17'))));
#(((('1','2'),'3'),(('4','5'),(('6','7'),'8'))),('9',(('10','11'),('12','13'))),('14',(('15','16'),'17')));
unrooted_trees_n17_Path = 'ut1_n_17.newick'
unrooted_trees_n17_PathRes = 'ut1_n_17.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_n17_Path, "-o", unrooted_trees_n17_PathRes])
#d_qt(T_1,T_2) = 286

# T_1\^u, T_2\^u rooted at the former neighbour of u=14 (n=16)
#((((('1','2'),('3','4')),((('5','6'),'7'),'8')),((('9','10'),'11'),('12','13'))),('15',('16','17')));
#((((('1','2'),'3'),(('4','5'),(('6','7'),'8'))),('9',(('10','11'),('12','13')))),(('15','16'),'17'));
rooted_trees_del_u_n16_Path = 'rt1_del_u_n_16.newick'
rooted_trees_del_u_n16_PathRes = 'rt1_del_u_n_16.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "tt", "-i", rooted_trees_del_u_n16_Path, "-o", rooted_trees_del_u_n16_PathRes])
#d_tt(T_1\^u, T_2\^u) = 26

# T_1|L\u, T_2|L\u with deleted u=14 (n=16)
#(((('1','2'),('3','4')),((('5','6'),'7'),'8')),((('9','10'),'11'),('12','13')),('15',('16','17')));
#(((('1','2'),'3'),(('4','5'),(('6','7'),'8'))),('9',(('10','11'),('12','13'))),(('15','16'),'17'));
unrooted_trees_del_u_n16_Path = 'ut1_del_u_n_16.newick'
unrooted_trees_del_u_n16_PathRes = 'ut1_del_u_n_16.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_del_u_n16_Path, "-o", unrooted_trees_del_u_n16_PathRes])
#d_qt(T_1|L\u, T_2|L\u) = 260

# 286 = 26 + 260