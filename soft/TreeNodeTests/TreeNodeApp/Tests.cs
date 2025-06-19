using Examples;
using PhyloTree;
using PhyloTree.Formats;

namespace TreeNodeApp
{
    internal static class Tests
    {
        public static void Test1(int min, int max, int step, double bifurcationProp = 0.0)
        {
            string[] labels = new string[max * 4];
            for (int i = 0; i < max * 4; i++)
            {
                labels[i] = i.ToString();
            }
            for (int leafNumbA = min; leafNumbA <= max; leafNumbA += step)
            {
                for (int leafNumbB = leafNumbA; leafNumbB <= max; leafNumbB += step)
                {
                    for (int leafNumbC = leafNumbB; leafNumbC <= max; leafNumbC += step)
                    {
                        for (int leafNumbD = leafNumbC; leafNumbD <= max; leafNumbD += step)
                        {
                            TreeNode subtreeA = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[0..leafNumbA], bifurcationProp);
                            TreeNode subtreeB = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[leafNumbA..(leafNumbA + leafNumbB)], bifurcationProp);
                            TreeNode subtreeC = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[(leafNumbA + leafNumbB)..(leafNumbA + leafNumbB + leafNumbC)], bifurcationProp);
                            TreeNode subtreeD = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[(leafNumbA + leafNumbB + leafNumbC)..(leafNumbA + leafNumbB + leafNumbC + leafNumbD)], bifurcationProp);

                            TreeNode firstTree = ComposeTree(subtreeA, subtreeB, subtreeC, subtreeD);
                            TreeNode secondTree = ComposeTree(subtreeA, subtreeB, subtreeD, subtreeC);
                            int distance = Math.Min(leafNumbA * leafNumbB * (leafNumbC + leafNumbD), leafNumbC * leafNumbD * (leafNumbA + leafNumbB));
                            NEXUS.WriteAllTrees([firstTree, secondTree], $"subtreeA{leafNumbA}_B{leafNumbB}_C{leafNumbC}_D{leafNumbD}_dist_{distance}.nex");
                        }
                    }
                }
            }
        }

        internal static void Test2(int maxLeafsOfTree, int maxRootDegOfSubtree, double bifurcationProp = 0.0)
        {
            int labelsCount = maxLeafsOfTree * 2;
            string[] labels = new string[labelsCount];
            for (int i = 0; i < labelsCount; i++)
            {
                labels[i] = i.ToString();
            }
            int minLeafNumb = 2;
            for (int leafNumbA = minLeafNumb; leafNumbA <= maxLeafsOfTree; leafNumbA++)
            {
                for (int leafNumbB = leafNumbA; leafNumbB <= maxLeafsOfTree; leafNumbB++)
                {
                    for (int rootDegOfSubtreeA = minLeafNumb; rootDegOfSubtreeA <= maxRootDegOfSubtree && rootDegOfSubtreeA <= leafNumbA; rootDegOfSubtreeA++)
                    {
                        List<TreeNode> subtreesOfA = GenerateSubtrees(bifurcationProp, labels, leafNumbA, rootDegOfSubtreeA, out List<int>  subtreesOfACardinality);
                        for (int rootDegOfSubtreeB = rootDegOfSubtreeA; rootDegOfSubtreeB <= maxRootDegOfSubtree && rootDegOfSubtreeB <= leafNumbB; rootDegOfSubtreeB++)
                        {
                            List<TreeNode> subtreesOfB = GenerateSubtrees(bifurcationProp, labels[leafNumbA..], leafNumbB, rootDegOfSubtreeB, out List<int> subtreesOfBCardinality);

                            TreeNode firstTree = new TreeNode(null);
                            firstTree.Children.AddRange(subtreesOfA);
                            firstTree.Children.AddRange(subtreesOfB);

                            TreeNode secondTree = new TreeNode(null);
                            TreeNode vNode = new TreeNode(secondTree);
                            secondTree.Children.Add(vNode);
                            vNode.Children.AddRange(subtreesOfA);
                            secondTree.Children.AddRange(subtreesOfB);

                            int distance1 = CardinalityOfUnions(subtreesOfACardinality) * CardinalityOfPairs(subtreesOfBCardinality) + CardinalityOfTriples(subtreesOfBCardinality);
                            int distance2 = CardinalityOfUnions(subtreesOfBCardinality) * CardinalityOfPairs(subtreesOfACardinality) + CardinalityOfTriples(subtreesOfACardinality);

                            int distance = Math.Min(distance1, distance2);

                            NEXUS.WriteAllTrees([firstTree, secondTree], $"leafA_{leafNumbA}_leafB_{leafNumbB}_rootDegA_{rootDegOfSubtreeA}_rootDegB_{rootDegOfSubtreeB}_dist_{distance}.nex");
                        }
                    }
                }
            }

            static List<TreeNode> GenerateSubtrees(double bifurcationProp, string[] labels, int leafNumbA, int rootDegOfSubtreeA, out List<int> subtreesCardinality)
            {
                List<TreeNode> subtrees = new();
                subtreesCardinality = new();

                for (int i = 0; i < rootDegOfSubtreeA; i++)
                {
                    int degOfSubtree = leafNumbA / rootDegOfSubtreeA;
                    int rangeBeg = degOfSubtree * i;
                    int rangeEnd = i == rootDegOfSubtreeA - 1 ? leafNumbA : degOfSubtree * (i + 1);
                    subtrees.Add(SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[rangeBeg..rangeEnd], bifurcationProp));
                    subtreesCardinality.Add(rangeEnd - rangeBeg);
                }
                return subtrees;
            }


            static int CardinalityOfUnions(List<int> subtreesCardinality)
            {
                int result = 0;
                for (int i = 0; i < subtreesCardinality.Count; i++)
                {
                    result += subtreesCardinality[i];
                }
                return result;
            }

            static int CardinalityOfPairs(List<int> subtreesCardinality)
            {
                int result = 0;
                for (int i = 0; i < subtreesCardinality.Count; i++)
                {
                    for (int j = 0; j < subtreesCardinality.Count; j++)
                    {
                        if (i < j)
                            result += subtreesCardinality[i] * subtreesCardinality[j];
                    }
                }
                return result;
            }

            static int CardinalityOfTriples(List<int> subtreesCardinality)
            {
                int result = 0;
                for (int i = 0; i < subtreesCardinality.Count; i++)
                {
                    for (int j = 0; j < subtreesCardinality.Count; j++)
                    {
                        for (int k = 0; k < subtreesCardinality.Count; k++)
                        {
                            if (i < j && j < k)
                                result += subtreesCardinality[i] * subtreesCardinality[j] * subtreesCardinality[k];
                        }
                    }
                }
                return result;
            }
        }

        private static TreeNode ComposeTree(TreeNode subtreeA, TreeNode subtreeB, TreeNode subtreeC, TreeNode subtreeD)
        {
            TreeNode uNode = new TreeNode(null);
            TreeNode vNode = new TreeNode(uNode);
            uNode.Children.Add(vNode);
            vNode.Children.Add(subtreeA);
            vNode.Children.Add(subtreeC);
            uNode.Children.Add(subtreeD);
            uNode.Children.Add(subtreeB);
            return uNode;
        }
    }
}
