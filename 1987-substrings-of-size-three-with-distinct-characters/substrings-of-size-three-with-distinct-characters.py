class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        count=0
        n=len(s)
        while right<n:
            if right-left+1==3:
                if s[left]!=s[left+1] and s[left+1]!=s[right] and s[left]!=s[right]:
                    count+=1
                left+=1
            right+=1
        return count
        