# 884. Uncommon Words from Two Sentences

## Problem

**Rating:** Easy

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is considered uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences `s1` and `s2`, return a list of all the uncommon words. The answer may be returned in any order.

### Example 1:

**Input:**  
`s1 = "this apple is sweet"`  
`s2 = "this apple is sour"`

**Output:**  
`["sweet", "sour"]`

**Explanation:**  
The word `"sweet"` appears only in `s1`, while `"sour"` appears only in `s2`.

### Example 2:

**Input:**  
`s1 = "apple apple"`  
`s2 = "banana"`

**Output:**  
`["banana"]`

**Constraints:**
- `1 <= s1.length, s2.length <= 200`
- `s1` and `s2` consist of lowercase English letters and spaces.
- There are no leading or trailing spaces.
- All words are separated by a single space.

## Solution

### Approach

We need to identify uncommon words between two sentences. A word is uncommon if:
1. It appears exactly once in either sentence.
2. It does not appear in both sentences.

### Algorithm

1. Split both sentences into words.
2. Combine the words from both sentences into a single list.
3. Count the occurrences of each word using a `Counter` from the `collections` module.
4. Filter out the words that appear exactly once from this combined list.

### Implementation

```python
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Step 1: Count occurrences of words in both sentences
        word_count = Counter(s1.split() + s2.split())
        
        # Step 2: Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
```

### Complexity Analysis

#### Time complexity:
The time complexity is `O(n)`, where n is the total number of words in both sentences combined. Splitting the sentences, counting the words, and filtering uncommon words all take linear time.

#### Space complexity:
The space complexity is `O(n)`, where n is the total number of words. We use extra space to store the list of words and the Counter for the frequency of each word.