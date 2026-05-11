class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False
        count_map = {}
        for num in nums:
            if num not in count_map.keys():
                count_map[num] = 1
            elif num in count_map.keys():
                hasDuplicate = True
        return hasDuplicate

        