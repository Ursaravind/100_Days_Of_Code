class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        additions = 0
        for char in s:
            if char == "(":
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    additions += 1
        return open + additions


obj = Solution()
print(obj.minAddToMakeValid(s=")))"))
