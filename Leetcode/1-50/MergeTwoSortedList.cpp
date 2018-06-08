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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
         ListNode* a = new ListNode(0); // a dummy
        ListNode* head = a;
        while(l1&&l2){
            if(l1->val > l2->val){
                a->next = new ListNode(l2->val);
                a = a->next;
                l2 = l2->next;
            }
            else{
                a->next = new ListNode(l1->val);
                a = a->next;
                l1 = l1->next;
            }
                
            }
        if(l1){
            a->next = l1;
        }
        if(l2){
            a->next = l2;
        }
            
        
        return head->next;
        
        
        
    }

       
};
