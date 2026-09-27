class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #    here the initial assumptions set can handle the cases like s = anagram , t = nagaram then set(s) = {a,n,g,r,m} , set(t) = {a,n,g,m,r} , the below code works in this case , but it failse when s = aacc , t = ccac , set(s) = ac, set(t) = ac , but we cannot form t from s , because we need three c's and one a from s
        #    set_s = set(s)
        #    set_t = set(t)
        #    for num in set_s:
        #     if num not in set_t:
        #         return False
        #    return True

        # Im thinking we need a frequency count , we just count both string characters count and then compare each string frequency
        # s = aacc , t = ccac
        # freq_s = {a:2,c:2} , freq_t = {c:3,a:1} , compare both we saw that freq_s.get(c) ! = freq_t.get(c) : return False
        # Approach -1
        # freq_s = {}
        # freq_t = {}
        # for char in s:
        #     freq_s[char] = freq_s.get(char, 0) + 1
        # for char in t:
        #     freq_t[char] = freq_t.get(char, 0) + 1
        # for char in freq_s.keys():
        #     if freq_s.get(char) != freq_t.get(char):
        #         return False
        # return True

        # Approach - 2
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in t:
            if char not in freq_s:
                return False
            freq_s[char] += -1
            if freq_s[char] < 0:
                return False
        return True
