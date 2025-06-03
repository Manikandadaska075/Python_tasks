class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next

def create_linked_list(arr):
    head = ListNode()
    current = head
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return head.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

list1 = list(map(int,input("Enter list 1 ").split()))
list2 = list(map(int,input("Enter list 2 ").split()))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print("Merged list:")
print_linked_list(merged)
