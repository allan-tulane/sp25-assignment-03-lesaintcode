# CMPS 2200 Assignment 3
## Answers

**Name:** Roberto Junqueira


Place all written answers from `assignment-03.md` here for easier grading.


- **1a:**  
Find the largest 2^k so that 2^k is less than or equal to N, then keep subtracting 2^k from N until N is less than or equal to 1.

- **1b:**  
We know that k is at its largest possible value every time because the highest value any of the coins can have still doesn't exceed N. This makes it optimal because if you don't you use more coins, there aren't any smaller coins to replace it.

- **1c:**  
Work: O(log N)  
Span: O(log N)

- **2a:**  
Counterexample: denominations [1,3,4], amount = 6.
Greedy algorithm yields coins [4,1,1] (3 coins total), but the optimal solution is [3,3] (2 coins total).

- **2b:**  
This problem has optimal substructure because solving for amount N optimally involves choosing a denomination and solving optimally for the remaining amount (N - denomination).
The optimal solution for the original problem necessarily includes optimal solutions for its subproblems.

- **2c:**  
A bottom-up dynamic programming approach involves computing the optimal number of coins required for each sub-amount from 0 to N, considering each denomination.
This approach has work and span complexity of O(N*k), where N is the target amount and k is the number of denominations.

- **3a:**  
Implemented top-down memoized solution (`fast_MED`) provided in Python (previously included).
