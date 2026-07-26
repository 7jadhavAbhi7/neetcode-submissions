# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev=None
        # curr=head
        # temp=head
        # while curr is not None:
        #     temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=temp
        # return prev

        stack=[]
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        n=ListNode(0)
        n1=n
        while stack:
            nn=ListNode(stack.pop())
            n.next=nn
            n=nn
        return n1.next


        