#Definition for singly-linked list.
def list2linkedList(list_val, node):
    temp_ln = node
    for i, val in enumerate(list_val):
        if i > 0:
            new_node = ListNode(val, None)
            temp_ln.next = new_node
            temp_ln = new_node

def print_list(node):
    temp_ln = node
    print(temp_ln.val)
    while temp_ln.next != None:
        temp_ln = temp_ln.next
        print(temp_ln.val)
    print("\n")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_node = ListNode(0, None)
        temp_node = first_node
        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1 != None or temp2 != None:
            x = temp1.val if temp1 is not None else 0
            y = temp2.val if temp2 is not None else 0
            sum =  x + y + temp_node.val
            temp_node.val = sum % 10
            carry = sum // 10

            if temp1 is not None:
                temp1 = temp1.next
            if temp2 is not None:
                temp2 = temp2.next

            if temp1 is not None or temp2 is not None:
                temp_node.next = ListNode(carry, None)
                temp_node = temp_node.next

        if carry == 1:
            temp_node.next = ListNode(carry, None)

        return first_node

list1 = [2,4,3]
list2 = [5,6,4]

list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]

l1 = ListNode(list1[0], None)
l2 = ListNode(list2[0], None)

list2linkedList(list1, l1)   # build a linked list
list2linkedList(list2, l2)   # build a linked list

print_list(l1)
print_list(l2)

res = Solution().addTwoNumbers(l1, l2)
print_list(res)