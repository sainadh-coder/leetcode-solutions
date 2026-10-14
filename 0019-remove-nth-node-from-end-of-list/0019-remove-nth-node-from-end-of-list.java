class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        int count = 0;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        if (count == n) {
            return head.next;
        }
        curr = head;
        for (int i = 1; i < count - n; i++) {
            curr = curr.next;
        }
        curr.next = curr.next.next;
        return head;
    }
}