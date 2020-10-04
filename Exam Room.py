from bisect import insort
class ExamRoom:

    def __init__(self, N: int):
        self.s=[]
        self.n=N

    def seat(self) -> int:
        if len(self.s)==0:
            self.s.append(0)
            return 0
        if len(self.s)==1:
            maxx=max(0,self.n-self.s[0]-1)
            insort(self.s,maxx)
            return maxx
        maxx=0
        maxl=0
        for i in range(1,len(self.s)):
            if self.s[i]-self.s[i-1]>maxx:
                maxx=self.s[i]-self.s[i-1]
                if maxx%2==0:
                    maxx+=1
                maxl=self.s[i-1]
        maxx=maxl+(maxx//2)
        insort(self.s,maxx)
        return maxx
        
    def leave(self, p: int) -> None:
        self.s.remove(p)

e=ExamRoom(10)
["ExamRoom","seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave","leave","seat","seat","leave","seat","leave","seat","leave","seat","leave","seat","leave","leave","seat","seat","leave","leave","seat","seat","leave"]
[[10],[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0],[4],[],[],[7 ],[],[3],[],[3],[],[9],[],[0],[8],[],[],[0],[8],[],[],[2]]