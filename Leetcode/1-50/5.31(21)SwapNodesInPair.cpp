/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL?true:head->next == NULL) return head;
        ListNode* dummy = new ListNode(0);
        swap(head,head->next,dummy);
        
        return dummy->next;

        
    }
    
    
    void swap(ListNode* first, ListNode* second, ListNode* pre){
        first->next = second->next;
        second->next = first;
        pre->next = second;
        if(first->next == NULL? false: first->next->next != NULL) swap(first->next,first->next->next,first);
        
        
    }
};
