# Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence

- **Date:** December 27, 2025
- **Difficulty:** Medium
- **Category:** Array / Hashmap
- **Time Taken:** N/A
- **Attempts:** 1
- **Status:** Done
---

## Summary
Find the length of the longest consecutive numbers in an unordered list

## Approach
We initialize a set to keep track of values we've already explored and to prevent going over duplicates. We find the first value by checking if i - 1 exists, if it does, it must be the value that we want to start from. From there while value + 1 exists, we're going to add to the length of the longest consecutive numbers. We then take the max of the current length with the last longest value. 

## Time Complexity: 
This algorithim runs O(n) time because it converts the list into a set in linear time, then iterates through each unique number once, and only begins counting the sequence when it finds the dtart of that sequence. Although we have a while loop, ever number is only visited once through all iterations becuase once a sequence is counted, its remaining elements will not trigger the start condition again.
## Space Complexity: 
This space compelexity is O(n) because we store all elements ina a set for constant-time lookups, while the remaining variable require only constant extra space

---

## Code
See solution.py

---

## Mistakes / What I learned
- 

