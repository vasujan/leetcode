from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = Counter(s1.split() + s2.split())  # Count words from both sentences
        return [word for word, count in word_count.items() if count == 1]
       