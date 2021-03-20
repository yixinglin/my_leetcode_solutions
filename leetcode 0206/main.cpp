#include <iostream>
#include <vector>
#include"tools.h"
#include "listnode.h"
using namespace std;


class Solution {
public:
    // 迭代法
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr, *curr = head, *next;
        while(curr != nullptr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};


int main()
{

    vector<int> arr({2, 3,5,7});
    ListNode *l1 = create_linked_list(arr);
    cout <<l1;

    ListNode *ans = Solution().reverseList(l1);
    cout <<ans;

    return 0;
}
