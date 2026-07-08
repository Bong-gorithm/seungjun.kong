# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head = ListNode(0)
        large_head = ListNode(0)

        small = small_head
        large = large_head
        current = head
        while current is not None:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next
            
            current = current.next
        
        # 연결
        large.next = None
        small.next = large_head.next

        return small_head.next