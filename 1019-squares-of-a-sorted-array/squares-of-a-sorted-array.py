class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            nums[i]=nums[i]*nums[i]
        left=0
        right=len(nums)-1
        new_arr=[None]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[left]>nums[right]:
                new_arr[i]=nums[left]
                left+=1
            else:
                
                new_arr[i]=nums[right]
                right-=1
            
        return new_arr
            
        