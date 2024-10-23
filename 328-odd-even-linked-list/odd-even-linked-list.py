class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        even_head = even  # To reconnect at the end

        while even and even.next:
            # Connect odd nodes together
            odd.next = even.next
            odd = odd.next

            # Connect even nodes together
            even.next = odd.next
            even = even.next

        # Link the end of odd nodes to the head of even nodes
        odd.next = even_head

        return head
