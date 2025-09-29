class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        '''my solution
        dictionary.sort(key= lambda x: (-len(x), x))
        for word in dictionary: 
            i = 0 
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                return word
        return ""
        '''
        # Sort the dictionary by length and lexicographically
        dictionary.sort(key=lambda x: (-len(x), x))
        
        # Traverse through the dictionary
        for word in dictionary:
            i = 0
            # Traverse through the string s
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
                    # If we have found all the characters in the word, break the loop
                    if i == len(word):
                        break
            # If we have found all the characters in the word, return the word
            if i == len(word):
                return word
        return ""