class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        res = []
        
        def isAnagram(s: str, t: str) -> bool:
        
            dictS = dict()

            for char in s:
                if char not in dictS:
                    dictS[char] = 0
                dictS[char] += 1

            for char in t:
                if char in dictS:
                    dictS[char] -= 1
                    if dictS[char] < 0:
                        return False
                else:
                    return False

            for val in dictS.values():
                if val != 0:
                    return False

            return True
        
        
        
        res.append([strs[0]])
        
        for currStr in strs[1:]:
            found = False
            for i in range(len(res)):
                if isAnagram(res[i][0], currStr):
                    res[i].append(currStr)
                    found = True
                    break
            if not found:
                res.append([currStr])
                #print(f'{currStr} is not a anagram of {res[i][0]}, appended {currStr} as a new entry, res= {res}')
                    
                    
        return res
        '''
        
        
        def encode(s):
            
            arr = [0]*26
            res = ''
            
            for char in s:
                arr[ord(char) - ord('a')] += 1
            #print(arr)
            for i in range(len(arr)):
                res += str(arr[i])+','
            return res
        
        
        lut = {}
        res = []
        for s in strs:
            code = encode(s)
            #print(f's={s},code={code}')
            if code not in lut:
                lut[code] = [s]
            else:
                lut[code].append(s)
        
        #print(lut)
        for item in lut.values():
            res.append(item)
            
        return res
        
        
        #res = encode('azcegaz')
        #print(res, type(res))
                
        
        
        
        