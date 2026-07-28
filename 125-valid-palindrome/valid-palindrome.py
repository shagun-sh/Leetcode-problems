class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=""
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()
        def helper(i):
            if(i>=len(clean)//2):
                return True
            if(clean[i]!=clean[len(clean)-i-1]):
                return False
            return helper(i+1)
        return helper(0)
        
    
        