class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # can it use a monotonic stack??
        """
        using indexes of the stack
        1) [0]
        2) [1]
        3) [2,1]
        4) [3, 1]  as 3 is greater than 2
        5) [4, 3, 1]
        6) [5]      as 5 is greater than all the ones in the stack
        7) [6, 5]
        """
        res = [0] * len(temperatures)
        stack = []

        l = 0
        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                pos = stack.pop()
                res[pos] = r - pos
            stack.append(r)
            print(f"stack: {stack}")
        return res


