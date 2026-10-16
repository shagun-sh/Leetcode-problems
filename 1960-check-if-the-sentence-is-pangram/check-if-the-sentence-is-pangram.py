class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
       
        unique_chars = {}

        for char in sentence:
            unique_chars[char] = True  
        total_unique = len(unique_chars)
    
        
        if total_unique==26:
            return True
        else:
            return False

            
            
        
        