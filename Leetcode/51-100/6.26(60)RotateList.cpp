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
    ListNode* rotateRight(ListNode* head, int k) {
        
        if(head == nullptr) return nullptr;
        
        int length = 1;
        ListNode* end = head;
        while(end->next != nullptr){
            end = end->next;
            length++;
        }
        
        int move = length - k % length;
        if(move == length ) return head;
        
        ListNode* pre = head;
        while(move != 1){
            pre = pre->next;
            move--;
        }
        ListNode* now = pre->next;
        end->next = head;
        pre->next = nullptr;
        
        return now;
    }
    
};
