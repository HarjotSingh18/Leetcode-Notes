class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[x] + nums[i] == target and x != i:
                    return [x, i]
