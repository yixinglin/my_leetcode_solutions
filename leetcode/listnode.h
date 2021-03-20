#include<vector>
#include<iostream>
#include<ostream>
/*
  Definition for singly-linked list.
*/
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode *create_linked_list(const std::vector<int> &vec) {
    int len = vec.size();
    ListNode *head = new ListNode(-1), *ptr = head;
    for(int i=0; i<len; i++) {
        ptr->next = new ListNode(vec[i]);
        ptr = ptr->next;
    }
    ptr = head->next;
    delete [] head;
    return ptr;
}

std::ostream &operator<<(std::ostream &out, ListNode *head) {
    ListNode *ptr = head;
    out << "[";
    while(ptr != nullptr) {
        int val = ptr->val;
        ptr = ptr->next;
        out<<val;
        if(ptr != nullptr)
            out<<", ";
    }
    out << "]" << std::endl;
    return out;
}
/*
    vector<int> arr1({0,2,3});
    ListNode *l1 = create_linked_list(arr1);
    cout << arr1<<arr1;
    cout <<l1;
*/
