from collections import deque

def can_complete_level(n, grid):
   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
  
    queue = deque([(0, 0)]) 
    visited = [[False] * n for _ in range(2)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
      
        if x == 1 and y == n - 1:
            return "YES"
        
      
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return "NO"


t = int(input())


for _ in range(t):
    n = int(input())  
    grid = [input().strip() for _ in range(2)]
    
 
    print(can_complete_level(n, grid))
