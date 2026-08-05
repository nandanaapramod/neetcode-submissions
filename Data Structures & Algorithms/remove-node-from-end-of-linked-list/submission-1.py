# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total=0
        cur=head

        while cur:
            total+=1
            cur=cur.next

        rmvInd=total-n
        if rmvInd==0:
            return head.next
        
        cur=head
        for i in range(total-1):
            if(i+1) == rmvInd:
                cur.next=cur.next.next
                break
            cur=cur.next
        return head