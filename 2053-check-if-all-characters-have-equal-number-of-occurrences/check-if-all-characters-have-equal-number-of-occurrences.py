class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq={}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        counts = list(freq.values()) 
        common=counts[0]
        for i in range(0,len(counts)):
            if counts[i]!=common:
                return False  
        return True