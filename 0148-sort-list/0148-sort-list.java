import java.util.*;
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        List<Integer> list = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            list.add(curr.val);
            curr = curr.next;
        }
        Collections.sort(list);
        curr = head;
        for (int val : list) {
            curr.val = val;
            curr = curr.next;
        }
        return head;
    }
}