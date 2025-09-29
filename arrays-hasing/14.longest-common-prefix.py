class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs, key = lambda x: len(x))
        sub_string = strs[0]
        i = 1
        while len(sub_string):
            if i == len(strs):
                break
            if strs[i].startswith(sub_string):
                i += 1
            else:
                i = 1
                sub_string = sub_string[:-1]
        return sub_string