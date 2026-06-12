class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for each in strs:
            res += each+"/#\\"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("/#\\")[:-1]
