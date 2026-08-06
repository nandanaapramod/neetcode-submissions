# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newlist=[]

        for l in lists:
            while l:
                newlist.append(l.val)
                l=l.next
        newlist.sort()

        linked=ListNode(0)
        cur=linked
        for n in newlist:
            cur.next=ListNode(n)
            cur=cur.next
        return linked.next
