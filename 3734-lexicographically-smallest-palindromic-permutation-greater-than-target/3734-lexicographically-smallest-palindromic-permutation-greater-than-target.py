class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Number of each character needed in the left half
        half = [x // 2 for x in cnt]
        half_len = n // 2

        left = []

        # Check whether the current prefix can be completed
        # into a palindrome > target.
        def possible():
            # Put remaining characters in descending order.
            # This gives the LARGEST possible completion.
            rem = []

            for i in range(25, -1, -1):
                if half[i]:
                    rem.append(chr(ord('a') + i) * half[i])

            candidate_left = ''.join(left) + ''.join(rem)

            # Build palindrome
            palindrome = (
                candidate_left
                + middle
                + candidate_left[::-1]
            )

            return palindrome > target

        # Build the left half greedily
        for _ in range(half_len):

            found = False

            # Try the smallest possible character first
            for c in range(26):

                if half[c] == 0:
                    continue

                # Choose this character
                half[c] -= 1
                left.append(chr(ord('a') + c))

                # Is there ANY completion that works?
                if possible():
                    found = True
                    break

                # This choice cannot lead to an answer
                left.pop()
                half[c] += 1

            if not found:
                return ""

        # Construct final palindrome
        left_half = ''.join(left)

        ans = left_half + middle + left_half[::-1]

        if ans > target:
            return ans

        return ""