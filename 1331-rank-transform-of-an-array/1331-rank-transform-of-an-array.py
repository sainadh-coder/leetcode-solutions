class Solution(object):
    def arrayRankTransform(self, arr):
        arr2 = arr[:]
        arr2.sort()

        ranks = {}

        if len(arr2) > 0:
            rank = 1
            ranks[arr2[0]] = rank

            for i in range(1, len(arr2)):
                if arr2[i] != arr2[i - 1]:
                    rank += 1
                ranks[arr2[i]] = rank

        return [ranks[x] for x in arr]