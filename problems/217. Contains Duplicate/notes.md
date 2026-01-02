https://leetcode.com/problems/contains-duplicate/

- **Date solved:**: December 28th, 2025
- **Difficulty:**: Easy
- **Category:**: Array & Hashing
- **Time taken:**: N/A
- **Attempts:**: 1
- **Language:**: Python
- **Status:**: 🟢
---

## Problem Summary

We're given a list of numbers, and we must return true if any number appears more than once within the list

---

## My Approach

- **Idea**: We create a int defaultdict that will keep the key as the number and value as the frequency of that number.
  
- **Why it works**: defaultdict creates a defaukt value for a key when it doesn't exist yet instead of throwing a KeyError

- **Time complexity**: This algorithm runs in O(n) time because it iterates through the list once to build the frequency dictionary and then scans the dictionary values once more to find the maximum count, both of which are linear operations.
  
- **Space complexity**:The space complexity is O(n) because the dictionary may store up to n unique elements, requiring memory proportional to the number of items in the input list.

---

## Code
See solution.py
