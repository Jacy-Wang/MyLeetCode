/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null || head.next == null)
            return head;
        ListNode dummy1 = new ListNode(0);
        dummy1.next = head;
        ListNode dummy2 = new ListNode(0);
        dummy2.next = null;
        ListNode node = dummy1;
        ListNode node2 = dummy2;
        while (node.next != null) {
            if (node.next.val >= x) {
                ListNode tmp = node.next.next;
                node.next.next = node2.next;
                node2.next = node.next;
                node2 = node2.next;
                node.next = tmp;
            } else {
                node = node.next;
            }
        }
        node.next = dummy2.next;
        return dummy1.next;
    }
}
