/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct ListNode* findMiddle(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        fast = fast->next->next;
        slow = slow->next;
    }
    if (prev) {
        prev->next = NULL;
    }
    return slow;
}

struct TreeNode* sortedListToBST(struct ListNode* head) {
    if (!head)
        return NULL;
    struct ListNode* mid = findMiddle(head);
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = mid->val;
    root->left = NULL;
    root->right = NULL;
    if (mid != head) {
        root->left = sortedListToBST(head);
    }
    root->right = sortedListToBST(mid->next);
    return root;
}