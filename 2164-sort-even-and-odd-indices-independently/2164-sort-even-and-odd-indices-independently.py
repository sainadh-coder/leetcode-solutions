class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        arr1 = [] 
        arr2 = [] 
        for i in range(len(nums)):
            if i % 2 == 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        arr1.sort()
        arr2.sort(reverse=True)
        ans = []
        p1, p2 = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(arr1[p1])
                p1 += 1
            else:
                ans.append(arr2[p2])
                p2 += 1
        return ans