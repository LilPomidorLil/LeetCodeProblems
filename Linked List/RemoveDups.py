# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next: ListNode  = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Если дан пустой список или дан список, содержащий один элемент, то возвращаем все без изменений
        if (not head) or (head.next == None):
            return head

        current: ListNode = head


        while (True):
            # если мы пришли в конец списка, то прерываемся

            if current.next == None:
                break

            # если текущее значение, равно следующему значению, то, мы идем на один элемент вперед и заменяем им
            # повторяющееся значение

            # иначе продолжаем исследование
            if (current.val == current.next.val):
                temporary: ListNode = current.next.next
                del current.next
                current.next = temporary
            else:
                current = current.next
        return head


if __name__ == '__main__':
    obj = Solution()
    head = ListNode()
    head.val = 1
    head.next = ListNode()
    head.next.val = 1
    head.next.next = ListNode()
    head.next.next.val = 3
    print(obj.deleteDuplicates(head))