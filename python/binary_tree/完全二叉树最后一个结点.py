from structure import TreeNode


def getLastNode(root: TreeNode) -> TreeNode:
    if root is None or root.left is None:
        return root
    lp, rp = root.left, root.right
    lh = rh = 0
    while lp:
        lp = lp.left
        lh += 1
    while rp:
        rp = rp.left
        rh += 1
    if lh > rh:
        return getLastNode(root.left)
    elif lh <= rh:
        return getLastNode(root.right)


if __name__ == '__main__':
    case1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3, TreeNode(6)))
    assert getLastNode(case1).val == 6
    case2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3, TreeNode(6), TreeNode(7)))
    assert getLastNode(case2).val == 7
    case3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                     TreeNode(3))
    assert getLastNode(case3).val == 5
    case4 = TreeNode(1,
                     TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10))),
                     TreeNode(3, TreeNode(6), TreeNode(7)))
    assert getLastNode(case4).val == 1
