class Solution:
    delimiter = "~"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for each in strs:
            _len = len(each)
            res += f"{_len}{self.delimiter}"+each
        print(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.delimiter:
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res




