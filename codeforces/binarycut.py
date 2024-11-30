"""
D. Binary Cut
time limit per test2 seconds
memory limit per test256 megabytes
You are given a binary string†
. Please find the minimum number of pieces you need to cut it into, so that the resulting pieces can be rearranged into a sorted binary string.


Note that:

each character must lie in exactly one of the pieces;
the pieces must be contiguous substrings of the original string;
you must use all the pieces in the rearrangement.
†
 A binary string is a string consisting of characters 0
 and 1
. A sorted binary string is a binary string such that all characters 0
 come before all characters 1
.

Input
The first line contains a single integer t
 (1≤t≤500
) — the number of test cases.

The only line of each test case contains a single string s
 (1≤|s|≤500
) consisting of characters 0
 and 1
, where |s|
 denotes the length of the string s
.

Output
For each test case, output a single integer — the minimum number of pieces needed to be able to rearrange the string into a sorted binary string.

Example
InputCopy
6
11010
00000000
1
10
0001111
0110
OutputCopy
3
1
1
2
1
2
Note
The first test case is pictured in the statement. It can be proven that you can't use fewer than 3
 pieces.

In the second and third test cases, the binary string is already sorted, so only 1
 piece is needed.

In the fourth test case, you need to make a single cut between the two characters and rearrange them to make the string 01
.
"""


def min_cuts_to_sorted(s):
    # If string is already sorted (all 0s or all 1s)
    if set(s) == {'0'} or set(s) == {'1'}:
        return 1

    # Count zeros and ones
    zeros = s.count('0')
    ones = len(s) - zeros

    # Initialize minimum pieces to a large value
    min_pieces = len(s)

    # Try all possible ways to distribute zeros
    for prefix_zeros in range(zeros + 1):
        # Calculate the number of others needed
        prefix_ones = zeros - prefix_zeros

        # Check if this distribution is valid
        if prefix_ones <= ones:
            # Count non-empty pieces
            pieces = (1 if prefix_zeros > 0 else 0) + \
                     (1 if prefix_ones > 0 else 0) + \
                     (1 if zeros - prefix_zeros > 0 else 0) + \
                     (1 if ones - prefix_ones > 0 else 0)

            # Update minimum pieces
            min_pieces = min(min_pieces, pieces)

    return min_pieces


# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input().strip()
    print(min_cuts_to_sorted(s))