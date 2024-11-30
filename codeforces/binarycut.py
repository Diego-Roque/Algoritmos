def min_cuts_to_sorted(s):
 
    if set(s) == {'0'} or set(s) == {'1'}:
        return 1
    
  
    zeros = s.count('0')
    ones = len(s) - zeros
    
  
    min_pieces = len(s)
    

    for prefix_zeros in range(zeros + 1):
      
        prefix_ones = zeros - prefix_zeros
        if prefix_ones <= ones:
            min_pieces = min(min_pieces, 
                             (1 if prefix_zeros > 0 else 0) + 
                             (1 if prefix_ones > 0 else 0) + 
                             (1 if zeros - prefix_zeros > 0 else 0) + 
                             (1 if ones - prefix_ones > 0 else 0))
    
    return min_pieces


t = int(input())
for _ in range(t):
    s = input().strip()
    
  
    print(min_cuts_to_sorted(s))
