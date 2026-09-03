class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations([], nums)

def permutations(p, up):
    if not up:
        return [p]

    ans = []

    ch = up[0]

    for i in range(len(p) + 1):
        f = p[:i]
        s = p[i:]
        ans += permutations(f + [ch] + s, up[1:])

    return ans