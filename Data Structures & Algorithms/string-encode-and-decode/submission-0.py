class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            output.append(s[i:j])
            i = j
        
        return output

