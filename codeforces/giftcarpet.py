def check_carpet(n, m, carpet):
 
    for c1 in range(m):
     
        v_rows = [r for r in range(n) if carpet[r][c1] == 'v']
        if not v_rows:
            continue
        
        for c2 in range(c1+1, m):
          
            i_rows = [r for r in range(n) if carpet[r][c2] == 'i']
            if not i_rows:
                continue
            
            for c3 in range(c2+1, m):
             
                k_rows = [r for r in range(n) if carpet[r][c3] == 'k']
                if not k_rows:
                    continue
                
                for c4 in range(c3+1, m):
                 
                    a_rows = [r for r in range(n) if carpet[r][c4] == 'a']
                    if not a_rows:
                        continue
                    
                    
                    for v_row in v_rows:
                        for i_row in i_rows:
                            if i_row == v_row:
                                continue
                            for k_row in k_rows:
                                if k_row == v_row or k_row == i_row:
                                    continue
                                for a_row in a_rows:
                                    if a_row == v_row or a_row == i_row or a_row == k_row:
                                        continue
                                    
                                 
                                    return "YES"
    
  
    return "NO"


t = int(input())
for _ in range(t):
   
    n, m = map(int, input().split())
    
  
    carpet = []
    for i in range(n):
        carpet.append(input().strip())
    
  
    print(check_carpet(n, m, carpet))
