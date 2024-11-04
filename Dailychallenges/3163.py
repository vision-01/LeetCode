class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        i=1
        cnt=1
        word_length=len(word)
        while i<word_length:          
            print(word[i-1],word[i])
            if word[i]==word[i-1] and cnt<9:
                cnt+=1
            else:
                comp+=str(cnt)+word[i-1]
                cnt=1
            i+=1
        if(word_length==1): 
            comp+=str(1)+word[0]
        else:
            if word[-1]==word[-2] and (cnt+1)<9:
                comp+=str(cnt)+word[-1]
            else:
                comp+=str(cnt)+word[-1]
        return comp


