from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        subs_len = word_len * len(words)
        result = []

        words_count = dict()
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        seen = dict()
        for i in range(0, len(s)):
            for j in range(i, i + subs_len, word_len):
                cur_word = s[j: j+word_len]
                if cur_word in words_count and words_count[cur_word] > 0:
                    words_count[cur_word] -= 1
                    seen[cur_word] = seen.get(cur_word, 0) + 1
                else:
                    break
            else:
                result.append(i)
            
            for word in seen:
                words_count[word] += seen[word]
            seen = dict()


        return result
            