class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s=[]
        summ=0
        for i in A:
            if i%2==0:
                summ+=i
        for i in queries:
            temp=A[i[1]]
            A[i[1]]+=i[0]
            if temp%2==0:
                if A[i[1]]%2==0:
                    summ+=i[0]
                else:
                    summ-=temp
            elif temp%2!=0 and A[i[1]]%2==0:
                summ+=temp+i[0]
            s.append(summ)
        return s