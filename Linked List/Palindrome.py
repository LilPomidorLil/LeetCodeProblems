# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

from typing import Optional
from SumList import func

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, slow):
        new_head = None
        while slow:
            slow.next, slow, new_head = new_head, slow.next, slow
        return new_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        if head.next is None:
            return True

        # находим середину отрезка, если длина нечетная, то возвращаем ложь
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # далее есть необходимость реверснуть одну из половин
        slow = self.reverse_list(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

if __name__ == '__main__':
    obj = Solution()
    head = [1, 0, 1]
    head = func(head)
    print(obj.isPalindrome(head))
