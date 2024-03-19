class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head