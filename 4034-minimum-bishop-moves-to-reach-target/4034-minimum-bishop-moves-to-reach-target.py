class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        p = abs(source[0]-target[0])
        q = abs(source[1]-target[1])
        if p==0 and q==0 : return 0
        if (source[0]+source[1])%2 != (target[0]+target[1])%2:
            return -1
        return 1 if p==q else 2