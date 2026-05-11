from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts_map = Counter(s)
        t_counts_map = Counter(t)
        if s_counts_map == t_counts_map:
            return True
        
        return False


