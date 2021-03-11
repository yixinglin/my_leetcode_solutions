#include <iostream>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *first_node = new ListNode(0);
        ListNode *temp_node = first_node;
        ListNode *temp1 = l1, *temp2 = l2;
        int carry = 0;

        while (temp1 != nullptr || temp2 != nullptr) {
            int x = temp1 != nullptr ? temp1->val: 0;
            int y = temp2 != nullptr ? temp2->val: 0;
            int sum = x + y + temp_node->val;
            temp_node->val = sum % 10;
            carry = sum / 10;

            if (temp1 != nullptr)
                temp1 = temp1->next;

            if (temp2 != nullptr)
                temp2 = temp2->next;

            if (temp1 != nullptr || temp2 != nullptr) {
                temp_node->next = new ListNode(carry);
                temp_node = temp_node->next;
            }


        }

        if (carry == 1)
            temp_node->next = new ListNode(carry);

        return first_node;

    }
};

int main()
{
    return 0;
}
