class Solution:        
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {};
        length = len(s);
        start = 0;
        ans = 0;
        for i,c in enumerate(s):
            if c in d:
                start = max(start, d[c]);
            d[c] = i+1;
            ans = max(ans, i - start + 1);
            print(ans);
            print(start,i);
        return ans;