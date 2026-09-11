class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        arr = []
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or i == k or j == k:
                        continue
                    num = digits[i]*100+digits[j]*10+digits[k]
                    if num>=100 and num%2==0:
                        arr.append(num)
        s = set(arr)
        return len(s)
        