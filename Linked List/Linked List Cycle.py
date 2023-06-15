from typing import (
    Any,
    Set,
    Optional,
)


class ListNode:
    def __init__(self, x) -> None:
        self.value: Any = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
        current = head
        visited_nodes: Set[ListNode] = set()
        
        while current:
            if current not in visited_nodes:
                visited_nodes.add(current)
            else:
                return True
            current = current.next
        return False