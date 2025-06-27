#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from pathlib import Path

treeCmpApp = '../../soft/TreeCmp/exe/TreeCmp-2.0-b103.jar'

# T_1A,T_2A,T_1B,T_2B rooted (n=6)
#(1,5,(4,(3,6,2)));
#(3,(4,(2,5),6,1));
#(12,(8,10,7,11),9);
#((12,9,8),(7,(10,11)));

# T_1A-T_1B,T_2A-T_2B unrooted (n=12)
#(1,5,(4,(3,6,2)),(12,(8,10,7,11),9));
#(3,(4,(2,5),6,1),((12,9,8),(7,(10,11))));

unrooted_trees_n12_Path = 'tress_n_u_12a.newick'
unrooted_trees_n12_PathRes = 'trees_n_u_12a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", unrooted_trees_n12_Path, "-o", unrooted_trees_n12_PathRes])
#m3(T_1A-T_1B,T_2A-T_2B) = 114

# K_A i K_B (n=20)
#(1,2,3,4,5,6);
#(7,8,9,10,11,12);

# T_1A-K_B,T_2A-K_B unrooted (n=12)
#(1,5,(4,(3,6,2)),(7,8,9,10,11,12));
#(3,(4,(2,5),6,1),(7,8,9,10,11,12));

unrooted_trees_takb_n12_Path = 'tress_n_takb_12a.newick'
unrooted_trees_takb_n12_PathRes = 'trees_n_takb_12a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", unrooted_trees_takb_n12_Path, "-o", unrooted_trees_takb_n12_PathRes])
#m3(T_1A-K_B,T_2A-K_B) = 58

# T_1B-K_A,T_2B-K_A unrooted (n=12)
#(12,(8,10,7,11),9,(1,2,3,4,5,6));
#((12,9,8),(7,(10,11)),(1,2,3,4,5,6));

unrooted_trees_tbka_n12_Path = 'tress_n_tbka_12a.newick'
unrooted_trees_tbka_n12_PathRes = 'trees_n_tbka_12a.out'
subprocess.check_call(["java", "-jar", treeCmpApp, "-m", "-d", "m3", "-i", unrooted_trees_tbka_n12_Path, "-o", unrooted_trees_tbka_n12_PathRes])
#m3(T_1B-K_A,T_2B-K_A) = 3423

# 114 = 58 + 56
