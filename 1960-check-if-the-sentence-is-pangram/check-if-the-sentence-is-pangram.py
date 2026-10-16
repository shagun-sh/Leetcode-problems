class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        unique=[]
        for i in sentence:
            unique.append(i)
            
        count=len(set(unique))
        if count==26:
            return True
        else:
            return False

            
            
        
        