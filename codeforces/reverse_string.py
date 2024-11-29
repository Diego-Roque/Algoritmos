def can_transform(s, t):
    n, m = len(s), len(t)
  
    for start in range(n):
    
        current = start
        
       
        collected = [s[current]]
        
       
        for right in range(current + 1, n):
            collected.append(s[right])
        
      
        for left in range(current - 1, -1, -1):
            collected.append(s[left])
        
      
        if ''.join(collected) == t:
            return True
    
    return False

q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    
   
    print("YES" if can_transform(s, t) else "NO")
