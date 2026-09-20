class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        xorr=0
        for num in nums:
            xorr^=num
        return xorr