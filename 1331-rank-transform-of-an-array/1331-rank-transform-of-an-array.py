class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr2 = arr[:]     
        arr2.sort()

        ranks = {}
        rank = 1

        for num in arr2:
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        ans = []
        for num in arr:
            ans.append(ranks[num])

        return ans