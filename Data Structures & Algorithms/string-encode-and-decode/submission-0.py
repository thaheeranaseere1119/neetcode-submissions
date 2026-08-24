class Solution:
  

    def encode(self, strs: List[str]) -> str:

        encode_str = ""

        for s in strs:
            l = len(s)

            encode_str += str(l)
            encode_str += '#'
            encode_str += s
  
        return encode_str       

    def decode(self, s: str) -> List[str]:

        decode_str = []
                                       
        i=0 
        j =1 

        while i<len(s):
            j=i

            while s[j]!= '#':
                j+=1                
            l = int(s[i:j])

            decode_str.append(s[ j+1 : j+1+l ])
            i = j+l+1
        return decode_str