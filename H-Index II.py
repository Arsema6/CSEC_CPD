class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def check(x):
            count =0
            for i in range(n-1,-1,-1):
                if citations[i] >=x:
                    count+=1
            return count >= x
        # return 0 if sum(citat)
        l,r = 0, n-1
        ans = n
        if citations[0] >= n:
            return n
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                l = mid+1
                ans = l
            else:
                ans = r
                r = mid-1
        return r

        
