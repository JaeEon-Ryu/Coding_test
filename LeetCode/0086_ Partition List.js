/*
Given the head of a linked list and a value x, 
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions. 
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {

    let partition1 = new ListNode();
    let partition2 = new ListNode();
    let temp1 = partition1, temp2 = partition2;

    while (head !== null) {
        if (head.val < x) {
            temp1.next = head;
            temp1 = temp1.next;
        }
        else {
            temp2.next = head;
            temp2 = temp2.next;
        }
        head = head.next;
    }
    temp1.next = null;
    temp2.next = null;

    temp1.next = partition2.next;
    return partition1.next

};
