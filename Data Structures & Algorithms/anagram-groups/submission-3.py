class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = []
        skip_idx = []
        for idx, str in enumerate(strs):
            counter = Counter(str)
            sub_list = [str]
            if idx in skip_idx:
                continue
            for idx2, str2 in enumerate(strs[idx + 1:len(strs)]):
                counter_other = Counter(str2)
                if counter_other == counter:
                    sub_list.append(strs[idx + 1 + idx2])
                    skip_idx.append(idx + 1 + idx2)
            counter_list.append(sub_list)
        return counter_list