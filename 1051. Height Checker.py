class Solution:
    def heightChecker(self, heights):
        s=[]
        c=0
        for i in heights:
            s.append(i)
        s.sort()
        for i in range(0,len(s)):
            if s[i]!=heights[i]:
                c+=1
        return c

if __name__=="__main__":
    l=str(input()[1:-1])
    l.strip("-")
    l=list(map(int,l.split(",")))
    s=Solution()
    print(s.heightChecker(l))