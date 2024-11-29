def solve_consecutive_removal(n, s):
  
    unique_strings = set()
    

    for i in range(n - 1):
        # Create a new string by removing characters at index i and i+1
        new_string = s[:i] + s[i+2:]
        unique_strings.add(new_string)
    
   
    return len(unique_strings)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
  
    print(solve_consecutive_removal(n, s))
