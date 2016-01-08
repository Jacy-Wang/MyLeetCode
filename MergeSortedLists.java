import java.util.Comparator;
import java.util.PriorityQueue;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
		PriorityQueue<ListNode> pq = new PriorityQueue<>(lists.length + 1, new Comparator<ListNode>(){
			@Override
			public int compare(ListNode o1, ListNode o2) {
				if (o1.val < o2.val) {
					return -1;
				}
				else if (o1.val > o2.val) {
					return 1;
				}
				return 0;
			}
		});
		for (int i = 0; i < lists.length; i++) {
			if (lists[i] != null) {
				pq.add(lists[i]);
			}
		}
		ListNode dummy = new ListNode(0);
		ListNode head = dummy;
		while (!pq.isEmpty()) {
			ListNode node = pq.poll();
			head.next = node;
			head = node;
			if (node.next != null) {
				pq.add(node.next);
			}
		}
		return dummy.next;        
    }
}
