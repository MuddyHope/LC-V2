class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')': "(", '}': "{", ']': '['}
        stack = []

        for each in s:
            if stack and stack[-1] == my_dict.get(each):
                stack.pop()
            else:
                stack.append(each) # usual stack append
        if stack:
            return False
        return True