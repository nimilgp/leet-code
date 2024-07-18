class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
