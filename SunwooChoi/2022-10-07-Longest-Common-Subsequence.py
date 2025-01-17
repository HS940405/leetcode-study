class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # track max common subsequence of substrings of text1 and text2
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range (len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                # if not matched, inherits prev max subsequence length
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[-1][-1]