https://leetcode.com/problems/valid-anagram/description/

- **Date solved:**: December 27th, 2025
- **Difficulty:**: Easy
- **Category:**: Array & Hashing
- **Time taken:**: N/A
- **Attempts:**: 1
- **Language:**: Python
- **Status:**: ✅
---

## Problem Summary
We're given two strings, t and s. We must return true of t is an anagram of s and false otherwise.

---

## My Approach

- Idea: We can sort the two strings alphabetically and see if the two strings equal each other
- Why it works: If two words are anagrams, they contain
    - the exact same characters
    - with the exact same frequencies
  Sorting rearranges characters into a fixed, predictable order (alphabetical order)
  Which allows us to see if the two strings equal to each other

- Time complexity: this algorithm takes O(n log n) time because sorting a string of length n requires O(n log n) operations, and this is done for both strings, but the dominant term remains O(n log n) overall.
- Space complexity: The space complexity is O(n) because sorting creates new lists of characters rather than modifying the strings in place, so the algorithm uses additional memory proportional to the number of characters in the strings.

---

## Code
See solution.py

