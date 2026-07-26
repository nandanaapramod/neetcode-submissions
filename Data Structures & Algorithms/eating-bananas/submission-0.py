class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        res=high

        while low<=high:
            kval=(low+high)//2

            hours=0
            for n in piles:
                hours+=math.ceil(float(n)/kval)
            if hours<=h:
                res=kval
                high=kval-1
            else:
                low=kval+1
        return res
