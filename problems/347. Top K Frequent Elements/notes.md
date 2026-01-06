# https://leetcode.com/problems/top-k-frequent-elements/description/

- **Date solved:**: January 5th, 2026
- **Difficulty:**: Medium
- **Category:**: Array & Hashing
- **Time taken:**: 23:02
- **Attempts:**: 3
- **Language:**: Python
- **Status:**: 🟢
---

## Problem Summary

- Given a integer array 'num' and an integer 'k', we want to return the
  'k' most frequent numbers in the array. We can return it in any order

---

## My Approach

- **Idea:** By using 'defaultdict' we can create a dictionary where each element in the array
  is assigned as a key with the value being the number of time it appears in the array. After that all
  we have to do is sort the array from highest to lowest value and take the top 'k' values. 
  
- **Why it works:** By transforming the input into a frequency map, we can isolate the count as a comparable metric. Sorting this map
  ensures that elements with the highest "count" metric are at the beginning of the list

- **Time complexity:** O(n log n) - Iterating through 'nums' to build the dictionary takes O(n), While sorting the items takes O(n log n) in
  the worst case(where all elements are unique) 
  
- **Space complexity:** O(n) - We store a dictionary dic which in the worst case holds 'n' unique elements if there are no duplicate
  

---

## Code
See solution.py
