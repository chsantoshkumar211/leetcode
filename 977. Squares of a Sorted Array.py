class Solution:
    def sortedSquares(self, A):
        s=[]
        for i in A:
            s.append(i*i)
        s.sort()
        print(s)

if __name__=="__main__":
    s=Solution()
    l=str(input()[1:-1])
    l.strip("-")
    l=list(map(int,l.split(",")))
    s.sortedSquares(l)