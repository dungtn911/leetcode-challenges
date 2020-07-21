Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        while head:
            res = res + pow(2,head.val)
            head = head.next
        return res
        
