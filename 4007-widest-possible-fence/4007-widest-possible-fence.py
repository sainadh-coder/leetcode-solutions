from collections import Counter, defaultdict

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq = Counter(planks)
        vals = sorted(freq.keys())
        m = len(vals)
        
        pair_count = defaultdict(int)
        
        # same-value pairs: v + v = 2v
        for v in vals:
            pair_count[2 * v] += freq[v] // 2
        
        # distinct-value pairs: v + w
        for i in range(m):
            v = vals[i]
            for j in range(i + 1, m):
                w = vals[j]
                pair_count[v + w] += min(freq[v], freq[w])
        
        ans = 0
        # baseline: just using originals as singles
        for v in vals:
            ans = max(ans, freq[v])
        
        # combine pairs + singles for every candidate target
        for T, pairs in pair_count.items():
            ans = max(ans, pairs + freq.get(T, 0))
        
        return ans