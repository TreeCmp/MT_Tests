using PhyloTree;
using PhyloTree.TreeBuilding;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;

namespace Examples
{
    internal static class SubtreeNodeGenerator
    {
        static Random RandomNumberGenerator = new ThreadSafeRandom();
        public static TreeNode GetSubtreeNode(string[] leafNames)
        {          
            int leafLength = leafNames.Length;
            TreeNode initialTree = new TreeNode(null);
            if (leafLength > 1)
            {
                initialTree.Children.Add(new TreeNode(initialTree));
                initialTree.Children.Add(new TreeNode(initialTree));
            }
            if (leafLength > 2)
            {                
                List<TreeNode> leaves = new List<TreeNode>();
                leaves.AddRange(initialTree.Children);

                while (leaves.Count < leafLength)
                {
                    int index = RandomNumberGenerator.Next(0, leaves.Count);
                    TreeNode selectedLeaf = leaves[index];
                    leaves.RemoveAt(index);
                    selectedLeaf.Children.Add(new TreeNode(selectedLeaf));
                    selectedLeaf.Children.Add(new TreeNode(selectedLeaf));
                    leaves.AddRange(selectedLeaf.Children);
                }
            }
            AddLeafNames(initialTree, leafNames);
            return initialTree;
        }

        private static void AddLeafNames(TreeNode tree, IReadOnlyList<string> leafNames)
        {
            List<TreeNode> leaves = tree.GetLeaves();
            List<string> leafNamesList = leafNames.ToList();

            for (int i = 0; i < leaves.Count; i++)
            {
                int index = RandomNumberGenerator.Next(0, leafNamesList.Count);
                leaves[i].Name = leafNamesList[index];
                leafNamesList.RemoveAt(index);
            }
        }
    }
}