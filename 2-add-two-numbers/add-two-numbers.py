
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize pointers and dummy head
        dummy_head = ListNode(0)
        current = dummy_head
        p, q = l1, l2
        carry = 0
        
        # Traverse both lists
        while p is not None or q is not None:
            # Extract current values or default to 0 if None
            x = p.val if p else 0
            y = q.val if q else 0
            
            # Calculate current sum and carry
            sum_val = carry + x + y
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            
            # Move to next nodes
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        
        # Handle final carry
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the result linked list, skipping the dummy head
        return dummy_head.next
