class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text=text.split()
        res=[]
        i=0
        while(i<len(text)-2):
            if text[i]==first and text[i+1]==second:
                res.append(text[i+2])
                i+=2
            else:
                i+=1
        return res