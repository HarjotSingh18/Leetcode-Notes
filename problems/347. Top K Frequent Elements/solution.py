class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic = defaultdict(int)
        answ = []

        for key in nums:
            dic[key] += 1

        sorted_items = sorted(dic.items(), key=itemgetter(1), reverse=True)

        for key, value in sorted_items[:k]:
            answ.append(key)
        
        return answ
