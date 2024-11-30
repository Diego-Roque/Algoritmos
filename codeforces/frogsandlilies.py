def min_jumps(n, d, lilies):
  
    lilies = list(map(int, list(lilies)))
    

    queue = [(0, 0)]  
    visited = set([0])
    
    while queue:
        current_pos, jumps = queue.pop(0)
        
     
        if current_pos == n - 1:
            return jumps
        
     
        for jump_length in range(1, d + 1):
            next_pos = current_pos + jump_length
            
           
            if (next_pos < n and 
                lilies[next_pos] == 1 and 
                next_pos not in visited):
                queue.append((next_pos, jumps + 1))
                visited.add(next_pos)
    
   
    return -1


n, d = map(int, input().split())
lilies = input().strip()


print(min_jumps(n, d, lilies))
