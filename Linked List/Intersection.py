# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional
from SumList import func

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def size(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA, sizeB = self.size(headA), self.size(headB)
        difference = abs(sizeA - sizeB)

        if sizeB > sizeA:
            while difference != 0:
                headB = headB.next
                difference -= 1
        else:
            while difference != 0:
                headA = headA.next
                difference -= 1

        while headB and headA:
            if headB == headA:
                return headA
            headA = headA.next
            headB = headB.next
        return None

if __name__ == "__main__":
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    listA = func(listA)
    listB = func(listB)

    obj = Solution()
    print(obj.getIntersectionNode(listA, listB))

