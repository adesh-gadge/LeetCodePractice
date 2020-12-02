import random 
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head
        
        while curr:
            if random.random() < 1/scope:
                chosen_value = curr.val
            curr = curr.next
            scope +=1 
        return chosen_value
        