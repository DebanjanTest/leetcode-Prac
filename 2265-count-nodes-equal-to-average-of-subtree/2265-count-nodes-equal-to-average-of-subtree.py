class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1

            if node.val == curr_sum // curr_count:
                self.count += 1

            return (curr_sum, curr_count)

        dfs(root)
        return self.count