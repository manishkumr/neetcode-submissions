class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = []
        is_consequetive = False
        cons_count = 0
        for num in nums:
            if num == 1:
                is_consequetive = True
                cons_count += 1
            else:
                max_ones.append(cons_count)
                is_consequetive = False
                cons_count = 0
        if cons_count > 0:
            max_ones.append(cons_count)

        max_ones.sort(reverse=True)
        return max_ones[0]




        