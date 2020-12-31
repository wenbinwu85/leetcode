class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linkedlist(node: ListNode) -> None:
    while node.next:
        print(node.val, end=' > ')
        node = node.next
    print(node.val)
    return None
