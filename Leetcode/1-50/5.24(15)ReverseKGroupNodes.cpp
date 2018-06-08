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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(!head) return NULL;
        if(k == 1) return head;
        int count = 0;
        ListNode* store = head;
        ListNode* a = head;
        ListNode* last;
        ListNode* firstpre = NULL;
        ListNode* first;
        ListNode* lastNext;
        head = NULL;
        while(a){
            
            count ++;
            if(count == 1){
                first = a;
            }
            
            
            if(count == k) {
                last = a;
                 a = a->next;
                count = 0;
                lastNext = last->next;
                last->next = NULL;
                reverse(first,lastNext);
                if(!head) head = last;
                if(!firstpre) firstpre = first;
                else {
                    firstpre->next = last;  
                    firstpre = first;
                }
            }
            else{
                 a = a->next;
            }
        }
        if(!head) return store;
        return head;        
    }
    
    ListNode* reverse(ListNode* cur, ListNode* pre ){
        ListNode* temp = cur->next;
        cur->next = pre;
        if(temp)return reverse(temp,cur);
        return cur;    
    }
};
