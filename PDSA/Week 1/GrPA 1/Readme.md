# Minimum Difference Among P Elements

## Problem Statement

Write a function `find_Min_Difference(L, P)` that:

- Accepts a list L of integers
- Accepts a positive integer P
- The size of L is greater than P

The task is to select P different elements from the list such that:

The difference between the maximum and minimum values in the selected subset is minimum among all possible subsets of size P.

The function should return this minimum difference value.

Note:
- There may be multiple subsets with the same minimum difference.
- Only return the minimum difference value.

---

## Example

Input:
L = [3, 4, 1, 9, 56, 7, 9, 12, 13]
P = 5

Output:
6

Explanation:

Possible subsets:
[3, 4, 7, 9, 9]
[7, 9, 9, 12, 13]

In both cases:
max - min = 6

---

## Approach

1. Sort the list.
2. Use a sliding window of size P.
3. For each window, compute:
   difference = L[i + P - 1] - L[i]
4. Return the minimum difference.

Time Complexity:
O(N log N)

---
