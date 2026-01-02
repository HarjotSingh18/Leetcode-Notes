https://leetcode.com/problems/group-anagrams/

- **Date solved:**: December 28th, 2025
- **Difficulty:**: Medium
- **Category:**: Array & Hashing
- **Time taken:**: 34:20
- **Attempts:**: 4
- **Language:**: Python
- **Status:**: 🟢
---

## Problem Summary

Given an array of strings strs, group the anagrams together. We return the answer in any order

---

## My Approach

- **Idea:** we're going to use list defaultdict and sorted. We'll set the keys to be the sorted string and the value to be the unsorted
  version of the string. 
  
- **Why it works:** defaultdict will assign the values to the correct sorted key. Once finished iterating through the list, we just need to
  return the values

- **Time complexity:** This algorithm runs in O(n · k log k) time because we iterate over all n strings and sort each one (which costs k log k)
  
- **Space complexity:** it uses O(n · k) space because the hashmap stores every string and its sorted-character key,
  requiring memory proportional to the total number of characters processed.
  

---

## Code
See solution.py
