/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        else {
            ListNode fast = head;
            ListNode slow = head;
            while (fast != null && fast.next != null) {
                fast = fast.next.next;
                slow = slow.next;
            }
            ListNode curTail = slow;
            ListNode node = slow.next;
            slow.next = null;
            ListNode nextNode;
            while (node != null) {
                nextNode = node.next;
                node.next = curTail;
                curTail = node;
                node = nextNode;
            }
            while (curTail != null) {
                if (head.val != curTail.val) {
                    return false;
                }
                head = head.next;
                curTail = curTail.next;
            }
            return true;
        }
    }
}