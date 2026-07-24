class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))

        pair = set()
        for x in vals:
            for y in vals:
                pair.add(x ^ y)

        ans = set()
        for p in pair:
            for x in vals:
                ans.add(p ^ x)

        return len(ans)
