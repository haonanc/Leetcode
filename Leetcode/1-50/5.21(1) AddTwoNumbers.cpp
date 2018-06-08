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
    
    
   void recursion(ListNode* l3, ListNode* l1, ListNode* l2, bool il1, bool il2, int passed){
       
       int total = 0;
       if(il1 == true){
           total += l1->val; 
       }
       
       if(il2 == true){
           total += l2->val;
       }
       total += passed;
       
       if(total >9){
           passed = 1;
           total = total - 10;
       }
       else{
           passed = 0;
       }
       
       l3->val = total;
       if(l1->next == NULL && l2->next == NULL && passed == 0){
           return;
       }
       else{
           ListNode* temp = new ListNode(0);
           l3->next = temp;
           l3 = temp;
       }
       if(l1->next != NULL){
           il1 = true;
           l1 = l1->next;
       }
       else{
           il1 = false;
       }
       if(l2->next != NULL){
           il2 = true;
           l2 = l2->next;
       }
       else{
           il2 = false;
       }
       recursion(l3,l1,l2,il1,il2,passed);
       
       
   }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode(0);
        recursion(temp, l1, l2, true, true, 0);
        return temp;
        }
        
        
    };
    
