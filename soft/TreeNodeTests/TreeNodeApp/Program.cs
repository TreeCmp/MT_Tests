using TreeNodeApp;

//Generates nexus files containing 2 trees
//between which exactly one NNI operation was performed.
//The cardinalities of the subtrees A, B, C, D
//and d_MT(T_1,T_2) = min {|A||B|(|C|+|D|),|C||D|(|A|+|B|))
//are encoded in the file names:
//subtreeA{leafNumbA}_B{leafNumbB}_C{leafNumbC}_D{leafNumbD}_dist_{distance}.nex"
//Tests.Test1(min: 1, max: 30, step: 1);
//Tests.Test1(min: 1, max: 30, step: 1, bifurcationProp: 0.7);


Tests.Test2(maxLeafsOfTree: 30, maxRootDegOfSubtree: 10);

