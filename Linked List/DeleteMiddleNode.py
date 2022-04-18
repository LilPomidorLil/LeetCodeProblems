# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
# instead you will be given access to the node to be deleted directly.

# guaranteed that the node to be deleted is not a tail node in the list.


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val: int = val
        self.next: ListNode = next


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val, node.next = node.next.val, node.next.next


# if __name__ == '__main__':
#     obj = Solution()
#     obj.deleteNode()

