class Solution(object):
    def isPalindrome(self, x):
        p = str(x)
        q = p[::-1]
        if p==q:
            return True
        else:
            return False   