class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        sum = requests[0]
        for i in range(1,len(requests)):
            sum+= abs(requests[i]-requests[i-1])
        return sum