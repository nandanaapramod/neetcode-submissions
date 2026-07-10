class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count={}
        for num in nums:
            count[num]=1+ count.get(num,0)
            
        temp=[]
        for num,c in count.items():
            temp.append([c,num])
        temp.sort()

        result=[]
        while len(result)<k:
            result.append(temp.pop()[1])
        return result