/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        if (head != null) {
            ListNode fast = head;
            ListNode slow = head;
            int counter = 1;
            while (fast.next != null && fast.next.next != null) {
                fast = fast.next.next;
                slow = slow.next;
                counter += 2;
            }
            while (fast.next != null) {
                fast = fast.next;
                counter += 1;
            }
            if (counter > 2) {
                // reverse second half of list
                ListNode p = slow.next;
                slow.next = fast;
                while (p != fast) {
                    ListNode nextNode = p.next;
                    p.next = fast.next;
                    fast.next = p;
                    p = nextNode;
                }
                // insert second half into first half
                ListNode h = head;
                ListNode node = null;
                int tmp = 0;
                while (tmp < (counter - 1) / 2) {
                    node = slow.next;
                    slow.next = node.next;
                    assert(h != null);
                    assert(node != null);
                    node.next = h.next;
                    h.next = node;
                    h = h.next.next;
                    tmp++;
                }
            }
        }
    }
}
