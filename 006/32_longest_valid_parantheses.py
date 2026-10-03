def longestValidParentheses(s: str) -> int:
    stack = [-1]
    res = 0
    for index, char in enumerate(s):
        if char == "(":
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                res = max(res, index - stack[-1])
    return res


print(longestValidParentheses(s="()(())"))
# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:

# Input: s = ""
# Output: 0
