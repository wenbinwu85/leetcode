from helper import ListNode, print_linkedlist


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                if not l1.next:
                    curr.next = l2
                    return head.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                if not l2.next:
                    curr.next = l1
                    return head.next
                l2 = l2.next
        return l1 or l2 or None


node1 = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(4)
node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node7

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

answer = Solution().mergeTwoLists(node1, node4)
print_linkedlist(answer)
