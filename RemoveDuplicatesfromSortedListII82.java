/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = head;
        ListNode slow = dummy;
        while (fast != null) {
            while(fast.next != null && fast.val == fast.next.val)
                fast = fast.next;
            if (fast == slow.next) {
                fast = fast.next;
                slow = slow.next;
            } else {
                slow.next = fast.next;
                fast = slow.next;
            }
        }
        return dummy.next;
    }
}
