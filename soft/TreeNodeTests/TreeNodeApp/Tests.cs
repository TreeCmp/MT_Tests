using Examples;
using MathNet.Numerics.Optimization;
using PhyloTree;
using PhyloTree.Formats;

namespace TreeNodeApp
{
    internal static class Tests
    {
        public static void Test1(int min, int max, int step)
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
                            TreeNode subtreeA = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[0..leafNumbA]);
                            TreeNode subtreeB = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[leafNumbA..(leafNumbA + leafNumbB)]);
                            TreeNode subtreeC = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[(leafNumbA + leafNumbB)..(leafNumbA + leafNumbB + leafNumbC)]);
                            TreeNode subtreeD = SubtreeNodeGenerator.GetSubtreeNode(leafNames: labels[(leafNumbA + leafNumbB + leafNumbC)..(leafNumbA + leafNumbB + leafNumbC + leafNumbD)]);

                            TreeNode firstTree = ComposeTree(subtreeA, subtreeB, subtreeC, subtreeD);
                            TreeNode secondTree = ComposeTree(subtreeA, subtreeB, subtreeD, subtreeC);
                            int distance = Math.Min(leafNumbA * leafNumbB * (leafNumbC + leafNumbD), leafNumbC * leafNumbD * (leafNumbA + leafNumbB));
                            NEXUS.WriteAllTrees([firstTree, secondTree], $"subtreeA{leafNumbA}_B{leafNumbB}_C{leafNumbC}_D{leafNumbD}_dist_{distance}.nex");
                        }
                    }
                }
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
