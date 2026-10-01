class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        is_valid = True
        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif stack and bracket_map.get(stack[-1]) == char:
                stack.pop()
            else:
                is_valid = False
                break
        return is_valid and not stack 