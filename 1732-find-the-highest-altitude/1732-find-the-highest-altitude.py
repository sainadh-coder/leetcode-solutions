class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        arr = [0]*(n+1)
        arr[0] = 0
        for i in range(1,n+1):
            arr[i] = gain[i-1]+arr[i-1]
        arr.sort()
        return arr[n]    

        