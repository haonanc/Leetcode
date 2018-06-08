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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head->next == NULL) return NULL;
        int b = recursion(head,NULL,n);
        if(b == -2) return head->next;
        return head;
        
    }
    
    int recursion(ListNode* cur, ListNode* pre,int n){
        //base case
        if(cur->next == NULL){
            if(n == 1){
                pre->next = NULL;
                return -1;
            }
            return 1;
        }
        int a = recursion(cur->next,cur,n);
        if(a == -1) return -1;
        a ++;
        if(a ==n){
            if(pre == NULL) return -2;
            pre->next = cur->next;
            return -1;
        }
        return a;
        
        
    }
};
