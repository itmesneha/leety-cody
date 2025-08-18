import collections
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], scores: List[int]) -> int:
        fmap = defaultdict(int)
        for letter in letters:
            fmap[letter] += 1
        self.res = 0

        def feasible(word, fmap):
            temp = defaultdict(int)
            for letter in word:
                temp[letter] += 1
                if temp[letter] > fmap[letter]:
                    return False
            return True

        def calculatescore(word, scores):
            res = 0
            for letter in word:
                res += scores[ord(letter) - ord('a')]
            return res

        def fn(words, idx, fmap, score):
            if idx >= len(words):
                self.res = max(self.res, score)
                return
            # if feasible, take it
            if feasible(words[idx], fmap):
                for letter in words[idx]:
                    fmap[letter] -= 1
                temp2 = calculatescore(words[idx], scores)
                score += temp2
                # explore forward
                fn(words, idx + 1, fmap, score)
                # backtrack
                for letter in words[idx]:
                    fmap[letter] += 1
                score -= temp2
            # or not take it
            fn(words, idx + 1, fmap, score)

        fn(words, 0, fmap, 0)
        return self.res