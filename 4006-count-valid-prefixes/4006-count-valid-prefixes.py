class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zercount = 0
        onecount = 0
        count = 0
        for i in range(len(s)):
            if(s[i]=='0'):
                zercount+=1
            if(s[i]=='1'):
                onecount+=1
            if(abs(zercount-onecount)==0 or abs(zercount-onecount)==1):
                count+=1
        return count
            