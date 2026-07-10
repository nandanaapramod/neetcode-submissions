class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       result=defaultdict(list)
       for i in strs:
            sorted_str=''.join(sorted(i))
            result[sorted_str].append(i)
       return list(result.values())
