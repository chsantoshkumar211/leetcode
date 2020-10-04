class Solution:
    def expressiveWords(self, s: str, words) -> int:
        c=0
        for w in words:
            i=0
            j=0
            check=0
            if len(s)<len(w):
                continue
            while i<len(s) and j<len(w):
                if s[i]!=w[j]:
                    check=1
                    break
                chars=0
                char=s[i]
                charw=0
                while i<len(s) and s[i]==char:
                    i+=1
                    chars+=1
                if chars<3:
                    while j<len(w) and w[j]==char:
                        charw+=1
                        j+=1
                    if chars!=charw:
                        check=1
                        break
                else:
                    while j<len(w) and w[j]==char:
                        j+=1
            if check==0 and i==len(s):
                c+=1
        return c
s="heeellooo"
words=["hello", "hi", "helo"]
print(Solution().expressiveWords(s,words))