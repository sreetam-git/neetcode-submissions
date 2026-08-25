class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            #find '#'
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            # now read the string of length 'length'

            word = s[j+1 : j + 1 + length]
            result.append(word)
            i = j + 1 + length
        
        return result



