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
    void reorderList(ListNode* head) {
        if(!head) return;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* slow = dummy;
        ListNode* fast = dummy;
        while(fast){
            if (!fast->next) break;
            fast = fast->next->next;
            slow = slow->next;
        }
        if(slow == head) return;
        fast = slow->next;
        slow->next = NULL;
        ListNode* end = reverse(fast,fast->next);
        fast->next = NULL;
        while(head){
            fast = head->next;
            head->next = end;
            if(!end)break;
            slow = end->next;
            end->next = fast;
            end = slow;
            head = fast;
        }
    }
    
    ListNode* reverse(ListNode* pre, ListNode* now){
        if(now == NULL){
            return pre;
        }
        ListNode* temp = now->next;
        now->next = pre;
        return reverse(now,temp);      
    }
};
