class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
       
        # unique_chars = {}

        # for char in sentence:
        #     unique_chars[char] = True  
        # total_unique = len(unique_chars)
    
        
        # if total_unique==26:
        #     return True
        # else:
        #     return False

        freq=[0]*26
        for i in sentence:
            index=ord(i)-ord('a') 
            freq[index]=1
        if sum(freq)==26:
            return True
        else:
            return False   
            
        
        