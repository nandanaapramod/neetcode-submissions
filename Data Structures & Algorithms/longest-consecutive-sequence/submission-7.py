class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        longest=0
        for i in nums:
            streak=0
            curr=i
            while curr in unique:
                streak+=1
                curr+=1
            longest=max(longest,streak)
        return longest