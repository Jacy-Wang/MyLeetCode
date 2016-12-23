tion for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null)
            return l1;
        if (l1 == null)
            return l2;
        if (l2 == null)
            return l1;
        if (l1.val == 0)
            return l2;
        if (l2.val == 0)
            return l1;
        int length1 = getLength(l1);
        int length2 = getLength(l2);
        /*if (length1 >= length2) {
            //ListNode longList = l1;
            ListNode shortList = l2;
        } else {
            ListNode longList = l2;
            ListNode shortList = l1;
        }*/
        /*int tmp = Math.abs(length1 - length2);
        ListNode head;
        ListNode node;
        ListNode carry;
        ListNode carryNode;
        boolean headSign = false;
        boolean carrySign = false;
        while (tmp > 0) {
            if (!headSign) {
                head = longList;
                longList = longList.next;
                headSign = true;
                node = head;
            } else {
                node.next = longList;
                longList = longList.next;
                node = node.next;
            }
            tmp--;
        }
        if (!headSign) {
            tmp = longList.val + shortList.val;
            if (tmp >= 10) {
                head = new ListNode(1);
                head.next = new ListNode(tmp % 10);
                node = head.next;
            } else {
                head = new ListNode (tmp);
                node = head;
            }
            headSign = true;
            longList = longList.next;
            shortList = shortList.next;
        }
        while (longList != null) {
            tmp = longList.val + shortList.val;
            if (tmp >= 10) {
                if (!carrySign) {
                    carrySign = true;
                    carry = new ListNode(1);
                    carryNode = carry;
                } else {
                    carryNode.next = new ListNode(1);
                    carryNode = carryNode.next;
                }
            } else {
                if (carrySign) {
                    carryNode.next = new ListNode(0);
                    carryNode = carryNode.next;
                }
            }
            node.next = new ListNode(tmp % 10);
            node = node.next;
            longList = longList.next;
            shortList = shortList.next;
        }

        return carrySign ? addTwoNumbers(head, carry) : head;*/
        return l1;
    }

    public int getLength(ListNode head) {
        ListNode node = head;
        int length = 0;
        while (node != null) {
            length++;
            node = node.next;
        }

        return length;
    }
}
