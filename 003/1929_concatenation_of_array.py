class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # Operator overloading / sequence repetition
        # 2 * 10 = 20
        # 2 * "abc" = "abcabc"
        # 2 * [1,2] = [1,2,1,2]
        return 2 * nums
