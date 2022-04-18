# https://leetcode.com/problems/partition-list/

# Given the head of a linked list and a value x, partition it such that all nodes less than x
# come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        after = after_head = ListNode()
        before = before_head = ListNode()

        while head.next is not None:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        before.next = after_head.next
        return before_head.next


def func(head):
    head_ = head_return =  ListNode()

    i = 0
    while i != len(head):
        head_.val = head[i]
        if i == len(head) - 1:
            return head_return
        head_.next = ListNode()
        head_ = head_.next
        i += 1



if __name__ == '__main__':
    obj = Solution()
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    head = func(head)
    obj.partition(head, 3)


