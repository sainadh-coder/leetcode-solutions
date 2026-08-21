import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            ans = 0
            for mask in range(1, 1 << len(coins)):
                l = 1
                bits = 0
                for i in range(len(coins)):
                    if mask & (1 << i):
                        bits += 1
                        l = l * coins[i] // math.gcd(l, coins[i])
                        if l > x:
                            break
                else:
                    if bits % 2:
                        ans += x // l
                    else:
                        ans -= x // l
            return ans
        low = 1
        high = min(coins) * k
        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low