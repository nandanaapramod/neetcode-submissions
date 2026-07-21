
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        out=[]

        for i in range(n):
            j=i+1
            count=1
            while j<n:
                if temperatures[j]>temperatures[i]:
                    break
                count+=1
                j+=1
            count=0 if j==n else count
            out.append(count)

        return out