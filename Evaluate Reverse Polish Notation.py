class Solution:
    def evalRPN(self, tokens) -> int:
        s=[]
        op=['*','-','+','/']
        for i in tokens:
            if i in op:
                l=s.pop()
                ll=s.pop()
                if i=='-':
                    temp=ll-l
                if i=='+':
                    temp=ll+l
                if i=='*':
                    temp=ll*l
                if i=='/':
                    sign=1
                    if ll<0:
                        sign*=-1
                    if l<0:
                        sign*=-1
                    temp=abs(ll)//abs(l)
                    temp*=sign
                s.append(int(temp))
            else:
                s.append(int(i))
        return s[0]
mat=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(mat))