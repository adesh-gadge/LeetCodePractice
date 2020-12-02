# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        #Converting linked list to an array
        self.l = [head.val]
        while head.next != None:
            
            head = head.next
            self.l.append(head.val)
    

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.l)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()