class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1 and l2 and l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            elif l1 and l2 and l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
    # def mergeTwoLists(self, l1, l2):
    #     new_list = []
    #     if len(l1) == 0:
    #         return l2
    #     elif len(l2) == 0:
    #         return l1
    #     else:
    #         for i, j in zip(l1, l2):
    #             if i <= j:
    #                 new_list.append(i)
    #                 new_list.append(j)
    #             else:
    #                 new_list.append(j)
    #                 new_list.append(i)
    #         return new_list


sol = Solution()
print(sol.mergeTwoLists([1,2,4], [2,4,5]))
