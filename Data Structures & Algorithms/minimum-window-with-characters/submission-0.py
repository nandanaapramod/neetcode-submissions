class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        count1={}
        for c in t:
            count1[c]=1+count1.get(c,0)
        
        need=len(count1)
        res=[-1,-1]
        reslen=float("infinity")
        window={}
        have=0
        l=0

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in count1 and window[c]==count1[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1

                window[s[l]]-=1

                if s[l] in count1 and window[s[l]]<count1[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if reslen!=float("infinity") else ""

