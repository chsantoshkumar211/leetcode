class Solution:
    def repeatedNTimes(self,a):
        for i in a:
            tcount=0
            for j in a:
                if i==j:
                    tcount+=1
            if tcount==len(a)/2:
                return i