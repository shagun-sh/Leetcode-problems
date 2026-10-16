class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
       
       

        freq=[0]*26
        for i in sentence:
            index=ord(i)-ord('a') 
            freq[index]=1
        if sum(freq)==26:
            return True
        else:
            return False   
            
        
        