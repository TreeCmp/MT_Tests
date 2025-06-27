#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

# T_1,T_2 rooted (n=16)
#((((8,9,(2,5,4,15)),(13,1,(6,12))),14,(16,11,7)),(10,3));
#(((10,(7,(4,6))),(5,(2,(16,13))),(14,12)),(9,8,(15,1),(3,11)));
rooted_trees_n16_Path = 'tress_n_16a.newick'
rooted_trees_n16_PathRes = 'trees_n_16a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "tt", "-i", rooted_trees_n16_Path, "-o", rooted_trees_n16_PathRes])
#d_tt(T_1,T_2) = 420

# U(T_1),U(T_2) unrooted (n=16)
#((((8,9,(2,5,4,15)),(13,1,(6,12))),14,(16,11,7)),10,3);
#((10,(7,(4,6))),(5,(2,(16,13))),(14,12),(9,8,(15,1),(3,11)));
unrooted_trees_n16_Path = 'tress_u_n_16a.newick'
unrooted_trees_n16_PathRes = 'trees_u_n_16a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_n16_Path, "-o", unrooted_trees_n16_PathRes])
#d_qt(U(T_1),U(T_2)) = 1445

# T_1K_1,B,T_2K_1,B dla B=(17,18,19,20);
#((((8,9,(2,5,4,15)),(13,1,(6,12))),14,(16,11,7)),(10,3),(17,18,19,20));
#(((10,(7,(4,6))),(5,(2,(16,13))),(14,12)),(9,8,(15,1),(3,11)),(17,18,19,20));
unrooted_trees_K1B_n20_Path = 'tress_n_20a.newick'
unrooted_trees_K1B_n20_PathRes = 'trees_n_20a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "qt", "-i", unrooted_trees_K1B_n20_Path, "-o", unrooted_trees_K1B_n20_PathRes])
#d_qt(T_1K_1,B,T_2K_1,B) = 3044

# 3125 = 4 * 420 + 1445