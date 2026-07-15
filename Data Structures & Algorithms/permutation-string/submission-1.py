class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        for c in s1:
            freq[c]=1+freq.get(c,0)
        need=len(freq)

        for i in range(len(s2)):
            count={}
            cur=0
            for j in range(i,len(s2)):
                count[s2[j]]=1+count.get(s2[j],0)
                if freq.get(s2[j],0) < count.get(s2[j]):
                    break
                if freq.get(s2[j],0) == count.get(s2[j]):
                    cur+=1
                if cur==need:
                    return True
        return False