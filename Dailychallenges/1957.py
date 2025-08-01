class Solution:
    def makeFancyString(self, s: str) -> str:
        result=''
        cnt=0
        prev=''
        for i in s:
            if(prev):
                if(prev==i):
                    cnt+=1
                else:
                    cnt=1
            if(cnt<3):
                result+=i
            prev=i
        return result