class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        
        while r>l:
            res_sum=numbers[l]+numbers[r]
            if res_sum > target:
                r-=1
            elif res_sum<target:
                l+=1
            else:
                return [l+1,r+1]
            
        return False