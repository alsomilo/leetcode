class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if not chars:
            return chars
        

        i,j = 0,0
        count = 0
        res = ''
        
        while j < len(chars):
            while j < len(chars) and chars[j] == chars[i]:
                count+=1
                j+=1
                
            if count > 1:
                res += chars[i] + str(count)
            else:
                res += chars[i]
                
            i = j
            count = 0
        
        #print(res)
                
        for i in range(len(res)):
            chars[i] = res[i]
            
        return len(res)
                
            

        
        
            