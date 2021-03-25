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
        if (!(head.next && head.val == head.next.val)) {
            temp.next = head;
            temp = temp.next;
        }
        head = head.next;
    }
    temp.next = null;

    return result.next;
};