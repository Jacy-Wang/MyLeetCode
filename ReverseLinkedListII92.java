/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n)
            return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int counter = 0;
        ListNode preNode = dummy;
        while (counter < m - 1) {
            counter++;
            preNode = preNode.next;
        }
        ListNode postNode = preNode.next;
        ListNode node = postNode.next;
        counter += 2;
        while (counter <= n) {
            counter++;
            ListNode tmp = node.next;
            node.next = preNode.next;
            preNode.next = node;
            node = tmp;
        }
        postNode.next = node;
        return dummy.next;
    }
}
