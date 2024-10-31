# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def treeQueries(self, roo: Optional[TreeNode], qry: List[int]) -> List[int]:  # noqa: F821
        def cal_dep(nod):
            if nod is None:
                return 0
            lft_dep, rgt_dep = cal_dep(nod.left), cal_dep(nod.right)
            dep_map[nod] = 1 + max(lft_dep, rgt_dep)
            return dep_map[nod]

        def dfs(nod, cur_dep, max_vis_dep):
            if nod is None:
                return
            cur_dep += 1
            res[nod.val] = max_vis_dep
            dfs(nod.left, cur_dep, max(max_vis_dep, cur_dep + dep_map[nod.right]))
            dfs(nod.right, cur_dep, max(max_vis_dep, cur_dep + dep_map[nod.left]))

        dep_map = defaultdict(int)
        cal_dep(roo)
        res = [0] * (len(dep_map) + 1)
        dfs(roo, -1, 0)
        return [res[val] for val in qry]
