class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        pref = [0] * (4 * n)
        suff = [0] * (4 * n)
        best = [0] * (4 * n)
        leftc = [''] * (4 * n)
        rightc = [''] * (4 * n)

        def pull(idx, l, r):
            mid = (l + r) // 2
            lc = idx * 2
            rc = idx * 2 + 1

            leftc[idx] = leftc[lc]
            rightc[idx] = rightc[rc]

            pref[idx] = pref[lc]
            if pref[lc] == mid - l + 1 and rightc[lc] == leftc[rc]:
                pref[idx] += pref[rc]

            suff[idx] = suff[rc]
            if suff[rc] == r - mid and rightc[lc] == leftc[rc]:
                suff[idx] += suff[lc]

            best[idx] = max(best[lc], best[rc])

            if rightc[lc] == leftc[rc]:
                best[idx] = max(best[idx], suff[lc] + pref[rc])

        def build(idx, l, r):
            if l == r:
                pref[idx] = suff[idx] = best[idx] = 1
                leftc[idx] = rightc[idx] = s[l]
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            pull(idx, l, r)

        def update(idx, l, r, pos, ch):
            if l == r:
                leftc[idx] = rightc[idx] = ch
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(idx * 2, l, mid, pos, ch)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, ch)

            pull(idx, l, r)

        build(1, 0, n - 1)

        ans = []

        for pos, ch in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, pos, ch)
            ans.append(best[1])

        return ans