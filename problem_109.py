# Convert Sorted List to Binary Search Tree - https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        nums = getList(head)
        return getTreeNode(nums, 0, len(nums) - 1)
        
def getTreeNode(nums, left, right):
    n = right - left + 1
    if n == 1:
        return TreeNode(nums[left])
    if n == 2:
        left_node = TreeNode(nums[left])
        right_node = TreeNode(nums[right])
        if left_node.val < right_node.val:
            right_node.left = left_node
            return right_node
        else:
            left_node.right = right_node
            return left_node
    mid = left + n / 2
    node = TreeNode(nums[mid])
    node.left = getTreeNode(nums, left, mid - 1)
    node.right = getTreeNode(nums, mid + 1, right)
    return node
        
def getList(head):
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res