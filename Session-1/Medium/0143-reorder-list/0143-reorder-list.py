# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 중간 찾기
        mid = head
        end = head

        while end and end.next:
            mid = mid.next
            end = end.next.next

        # 리스트 뒤집기
        back = mid.next
        mid.next = None

        prev = None
        current = back

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        reversed_back = prev

        # 리스트 합치기
        front = head
        back = reversed_back

        while back:
            front_next = front.next
            back_next = back.next

            front.next = back
            back.next = front_next

            front = front_next
            back = back_next
        