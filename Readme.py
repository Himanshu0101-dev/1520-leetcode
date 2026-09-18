class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)
        first = {}
        last = {}
        
        # Step 1: record first and last occurrence
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        
        intervals = []
        
        # Step 2: expand intervals
        for ch in set(s):
            i, j = first[ch], last[ch]
            k = i
            valid = True
            while k <= j:
                if first[s[k]] < i:
                    valid = False
                    break
                j = max(j, last[s[k]])
                k += 1
            if valid:
                intervals.append((i, j))
        
        # Step 3: greedy selection
        intervals.sort(key=lambda x: x[1])  # sort by end index
        res = []
        prev_end = -1
        for i, j in intervals:
            if i > prev_end:
                res.append(s[i:j+1])
                prev_end = j
        return res
