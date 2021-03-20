#include <iostream>
#include <vector>
#include"tools.h"
#include "listnode.h"
using namespace std;

int main()
{

    vector<int> arr1({0,2,3}), arr2({3,2,5,7});
    ListNode *l1 = create_linked_list(arr1);
    ListNode *l2 = create_linked_list(arr2);

    cout <<l1; cout <<l2;

    cout << "Hello world!" << endl;
    return 0;
}
