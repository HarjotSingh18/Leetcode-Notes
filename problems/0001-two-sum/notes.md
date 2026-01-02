# Two Sum
https://leetcode.com/problems/two-sum/

- **Date:** January 1st, 2026
- **Difficulty:** Easy
- **Category:** Array / Hashmap
- **Time Taken:** 32:37
- **Attempts:** 1
- **Status:** Need To Review

---

## Summary
Find the indexes of two numbers from some list that add up to a given target value

## Approach
Using a nested loop, we can compare an first value with the rest of the values in the lists and see if they add up to the target value. If they do not, the first loop will move on to the next value and compare itself with the rest of the values again until a solution is found.

## Time Complexity: 
O(n²) - There are two for loops that each iterate over the list 
## Space Complexity: 
O(n) - the algorithm doesn’t create any data structures that grow with the size of the input; it only uses a few variables.

---

## Code
See solution.py

---

## Mistakes / What I learned
- Using a nested for loop causes n x n pairs to be explored in the worst case causing the code to run inefficient and slow
