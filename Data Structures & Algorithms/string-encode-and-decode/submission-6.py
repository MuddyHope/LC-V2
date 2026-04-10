class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for each in strs:
            res += each+"/#\\"
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("/#\\")[:-1]