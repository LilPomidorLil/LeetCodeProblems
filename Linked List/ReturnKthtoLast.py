# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # для начала, нам нужно посчитать, сколько узлов нам необходимо пройти до энного узла, чтобы его удалить

        count = 0
        tmp = head

        while tmp:
            count += 1
            tmp = tmp.next


        # сделаем проверку на то, что энный элемент совпадает с длиной списка

        if (count == n):
            return head.next


        # теперь нам нужно дойти до того узла, который будем удалять, а точнее, остановиться перед ним
        temporary = head
        for i in range(count - n - 1):
            temporary = temporary.next

        # собственно удаление узла
        temporary.next = temporary.next.next
        return head





if __name__ == '__main__':
    obj = Solution()
    head = ListNode()
    head.val = 1
    head.next = ListNode()
    head.next.val = 1
    head.next.next = ListNode()
    head.next.next.val = 3
    obj.removeNthFromEnd(head, 1)
