class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        strings = {word: i for i, word in enumerate(words)}
        result = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                rev_prefix, rev_suffix = prefix[::-1], suffix[::-1]
                if rev_prefix in strings and strings[rev_prefix] != i and suffix == rev_suffix: 
                    result.append([i, strings[rev_prefix]])
                if j and rev_suffix in strings and strings[rev_suffix] != i and prefix == rev_prefix: 
                    result.append([strings[rev_suffix], i])
        return result