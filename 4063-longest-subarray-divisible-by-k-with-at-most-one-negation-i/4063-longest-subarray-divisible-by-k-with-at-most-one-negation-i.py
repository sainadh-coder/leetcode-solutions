class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        # Check all possible starting points l
        for l in range(n):
            current_sum = 0
            # Track the set of values (2 * nums[t]) % k seen so far in nums[l..r]
            seen_two_x = set()
            
            for r in range(l, n):
                val = nums[r]
                current_sum += val
                seen_two_x.add((2 * val) % k)
                
                # Check condition 1: sum is directly divisible by k
                # Check condition 2: sum == 2 * nums[t] (mod k) for some t in [l, r]
                rem = current_sum % k
                if rem == 0 or rem in seen_two_x:
                    ans = max(ans, r - l + 1)
                    
        return ans