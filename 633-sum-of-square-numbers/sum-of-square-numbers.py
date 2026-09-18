class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        R=int(c**0.5)
        L=0
        while(L<=R):
            if(L**2+R**2)<c:
                L+=1
            elif(L**2+R**2)>c:
                 R-=1
            else:
                return True
        return False

            