class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dic = defaultdict(int)

        for key in nums:
            dic[key] += 1

        if max(dic.values()) > 1:
            return True
        else:
            return False
        
