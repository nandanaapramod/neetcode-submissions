class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        longest=0

        for n in unique:
            if (n-1) not in unique:
                length=1
                while (n+length) in unique:
                    length+=1
                longest=max(longest,length)
        return longest
