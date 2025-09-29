class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        new_strs = {}
        final_strs = []
        index = 0
        for word in strs:
            sorted_word = " ".join(sorted(word))
            if sorted_word not in new_strs:
                new_strs[sorted_word] = index
                final_strs.append([word])
                index += 1
            else:
                final_strs[new_strs[sorted_word]].append(word)
        return final_strs
        ''' time complexity is O(m + n)
        res = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in res:
                res[key] = [ word ]
            else:
                res[key].append(word)
        return list(res.values)
        '''