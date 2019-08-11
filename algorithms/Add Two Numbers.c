/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
        
    struct ListNode* start = malloc(sizeof(struct ListNode));
    int ans = (l1->val+l2->val);
    int carry = 0;
    if(ans>=10){
        carry = 1;
    }
    ans%=10;
    start->val=ans;
    struct ListNode* prev = start;
    while(l1->next!=NULL&&l2->next!=NULL){
        l1=l1->next;
        l2=l2->next;
        struct ListNode* node = malloc(sizeof(struct ListNode));
        int ans = (l1->val+l2->val)+carry;
        carry=0;
        if(ans>=10){
            carry = 1;
        }
        ans%=10;
        node->val=ans;
        prev->next=node;
        prev=node;
    }
    while(l1->next!=NULL){
        l1=l1->next;
        struct ListNode* node = malloc(sizeof(struct ListNode));
        int ans = (l1->val)+carry;
        carry=0;
        if(ans>=10){
            carry = 1;
        }
        ans%=10;
        node->val=ans;
        prev->next=node;
        prev=node;
    }
    while(l2->next!=NULL){
        l2=l2->next;
        struct ListNode* node = malloc(sizeof(struct ListNode));
        int ans = (l2->val)+carry;
        carry=0;
        if(ans>=10){
            carry = 1;
        }
        ans%=10;
        node->val=ans;
        prev->next=node;
        prev=node;
    }
    if(carry==1){
        struct ListNode* node = malloc(sizeof(struct ListNode));
        node->val=1;
        node->next=NULL;
        prev->next=node;
        return start;
    }
    prev->next=NULL;
    return start;
}