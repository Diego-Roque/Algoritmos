"""
A. Append and Panic!
time limit per test 0.5 seconds
memory limit per test 1024 megabytes
Today is Gabriel's first day at his new job, and he has been given his first task. He needs to read a string made up of uppercase letters from a file, sort the letters in the string alphabetically, filter out repeated letters, and then write the result back to the original file. For instance, sorting the string "ICPC" would produce "CCIP", which would become "CIP" after removing repeated letters. Easy, right?

However, Gabriel made a tiny mistake. Instead of overwriting the file with the filtered string, he accidentally appended it to the file. Now, the file is corrupted, containing the original string followed by the sorted, duplicate-free version of it, and Gabriel is in a bit of a panic.

Given the content of the corrupted file, can you determine the length of the original string? Gabriel is confident that with this information, he will be able to complete his assigned task.

Input
The input consists of a single line that contains a string S
 made up of uppercase letters (2≤|S|≤2000
), which is the concatenation of the original (uncorrupted) string t
 and the sorted, duplicate-free version of t
.

Output
Output a single line with an integer indicating the length of t
.

Examples
Input
ICPCCIP
Output
4
Input
ABEDCCCABCDE
Output
7
Input
ZZ
Output
1


"""

def find_original_length(S):
    # Set to store the unique characters
    seen = set()
    unique_length = 0

    # Traverse from the end to find the sorted, duplicate-free version
    for i in range(len(S) - 1, -1, -1):
        if S[i] not in seen:
            seen.add(S[i])
            unique_length += 1
        else:
            break

    # The length of the original string t is the total length minus the length of the sorted unique part
    return len(S) - unique_length

# Input the concatenated string
S = input()
# Output the length of the original string
print(find_original_length(S))
