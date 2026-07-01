/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        Set<Integer> seen = new LinkedHashSet<>();

        // Extract all values from the linked list
        while (head != null) {
            seen.add(head.val); // HashSet removes duplicates
            head = head.next;
        }

        // Create a new linked list from the set
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int val : seen) {
            current.next = new ListNode(val);
            current = current.next;
        }

        return dummy.next;
    }
}
