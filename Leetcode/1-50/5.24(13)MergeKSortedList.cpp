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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return NULL;
        int q;
        while(lists.size() !=1){
            q = 0;
            while(q + 1< lists.size()){
                lists[q] = merge(lists[q],lists[q+1]);
                lists.erase(lists.begin()+q+1);
                q++;
            }
            
        }
        return lists[0];
    }
    
    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode* a = new ListNode(0); // a dummy
        ListNode* head = a;
        while(true){
            if(l1 == NULL && l2 == NULL){
                break;
            }
            else if(l1 == NULL){
                a->next = new ListNode(l2->val);
                a = a->next;
                l2 = l2->next;
            }
            else if(l2 == NULL){
                a->next = new ListNode(l1->val);
                a = a->next;
                l1 = l1->next;
            }
            else{
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
            
        }
        return head->next;
    }
};
