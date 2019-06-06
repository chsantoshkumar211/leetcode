class Solution:
    def majorityElement(self, nums):
        stack=[]
        count={}
        for i in nums:
            if i not in stack:
                stack.append(i)
                c=nums.count(i)
                count[i]=c
        maxc=count[stack[0]]
        maxe=stack[0]
        for key in count:
            if count[key]>maxc:
                maxe=key
                maxc=count[key]
        return maxe

if __name__=="__main__":
    l=list(input()[1:-1])
    while(l.count(",")!=0):
        l.remove(",")
    s=Solution()
    s.majorityElement(l)