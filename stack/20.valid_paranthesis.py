class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        h = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        # this gives us a way to keep track of other side, but also 
        # have value to compare to when using lifo of stack
       
        for char in s:
            if char in h.keys():
                stk.append(h[char])
            else:
                if stk:
                    curr = stk.pop()
                else: return False
                if curr != char:
                    return False
        if stk:
            return False

        return True