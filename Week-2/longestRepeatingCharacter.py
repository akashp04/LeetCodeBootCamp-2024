class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, result, j = {}, 0, 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            if (i - j + 1) - (max(count.values())) > k:
                count[s[j]] -= 1
                j += 1
            result = max(result, i - j + 1)
        return result