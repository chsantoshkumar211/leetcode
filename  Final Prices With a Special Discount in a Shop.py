class Solution:
    def finalPrices(self, prices):
        q=[]
        tot=0
        res=[-1]*len(prices)
        i=0
        while i<len(prices):
            while q and prices[q[-1]]>=prices[i]:
                res[q[-1]]=prices[q[-1]]-prices[i]
                q.pop()
            q.append(i)
            i+=1
        for i in range(len(res)):
            if res[i]==-1:
                res[i]=prices[i]
        return res

mat=[10,1,1,6]
print(Solution().finalPrices(mat))