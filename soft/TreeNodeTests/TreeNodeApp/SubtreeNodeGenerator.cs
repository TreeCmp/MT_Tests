using PhyloTree;
using PhyloTree.TreeBuilding;

namespace Examples
{
    internal static class SubtreeNodeGenerator
    {
        static Random RandomNumberGenerator = new ThreadSafeRandom();
        public static TreeNode GetSubtreeNode(string[] leafNames, double bifurcationProp = 0.0)
        {   
            int leafNumber = leafNames.Length;
            TreeNode initialTree = new TreeNode(null);
            int currentLeavesNumber = 1;
            if (leafNumber > 1)
            {
                initialTree.Children.Add(new TreeNode(initialTree));
                initialTree.Children.Add(new TreeNode(initialTree));
                currentLeavesNumber++;
                while (currentLeavesNumber < leafNumber &&
                    RandomNumberGenerator.NextDouble() < bifurcationProp)
                {
                    currentLeavesNumber++;
                    initialTree.Children.Add(new TreeNode(initialTree));
                }
            }
            if (leafNumber > 2)
            {                
                List<TreeNode> leaves = new List<TreeNode>();
                leaves.AddRange(initialTree.Children);

                while (leaves.Count < leafNumber)
                {
                    int index = RandomNumberGenerator.Next(0, leaves.Count);
                    TreeNode selectedLeaf = leaves[index];
                    leaves.RemoveAt(index);
                    selectedLeaf.Children.Add(new TreeNode(selectedLeaf));
                    selectedLeaf.Children.Add(new TreeNode(selectedLeaf));
                    currentLeavesNumber++;
                    while (currentLeavesNumber < leafNumber &&
                        RandomNumberGenerator.NextDouble() < bifurcationProp)
                    {
                        selectedLeaf.Children.Add(new TreeNode(selectedLeaf));
                        currentLeavesNumber++;
                    }
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