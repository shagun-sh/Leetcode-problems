class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        right=0
        total=0
        maxsum=float('-inf')
        while right<len(nums):
            total=total+nums[right]
            if right-left+1==k:
                maxsum=max(maxsum,total)
                total=total-nums[left]
                left=left+1
            right=right+1
        return float(maxsum)/k
        