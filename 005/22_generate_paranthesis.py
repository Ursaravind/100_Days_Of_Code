def generateParenthesis(n: int) -> list[str]:
    result = []

    def back_track(path, open, close):
        if len(path) == 2 * n:
            result.append("".join(path))
        if open < n:
            path.append("(")
            back_track(path, open + 1, close)
            path.pop()
        if close < open:
            path.append(")")
            back_track(path, open, close + 1)
            path.pop()

    back_track([], 0, 0)
    return result


print(generateParenthesis(n=3))
