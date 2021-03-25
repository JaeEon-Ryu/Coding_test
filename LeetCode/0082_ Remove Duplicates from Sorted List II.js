/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {

    if (head == undefined) return head;

    let result = new ListNode();
    let temp = result;
    let cnt = 0;

    while (head !== null) {
        if (head.next && head.val == head.next.val) {
            cnt++;
        }
        else {
            if (cnt == 0) {
                temp.next = head;
                temp = temp.next;
            }
            cnt = 0;
        }
        head = head.next;
    }
    temp.next = null;

    return result.next;
};