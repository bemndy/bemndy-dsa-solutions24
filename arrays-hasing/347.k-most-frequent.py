class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        s = {}
        for num in nums:
            if num in s:
                s[num] += 1
            else: 
                s[num] = 1
        '''
            s[num] = 1 + count.get(num, 0)
        '''
        s = sorted(s, key=lambda k: s[k], reverse=True)
        return s[:k]
        ''' neetcode solution with bucket sort
        count = {}
        freq = [ [] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, value in count.items():
            freq[values].append(key)
        res = []
        for i in range(len(nums)-1, 0, -1):
            for n in freq[i]:
                res.append(value)
                if i == k: 
                    return freq
        '''