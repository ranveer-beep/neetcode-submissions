class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"(":")", "{":"}", "[":"]"}
        stack = []

        for ch in s:
            if ch in matching:
                stack.append(ch)
            else:
                if stack and matching[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return not stack