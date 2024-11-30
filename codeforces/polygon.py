def can_form_matrix(n, matrix):
 
    for i in range(n - 1):
        for j in range(n - 1):
          
            if matrix[i][j] == '1':
             
                if matrix[i + 1][j] != '1' and matrix[i][j + 1] != '1':
                    return "NO"
    return "YES"


t = int(input().strip())
results = []

for _ in range(t):
  
    n = int(input().strip())
 
    matrix = [input().strip() for _ in range(n)]
   
    results.append(can_form_matrix(n, matrix))


print("\n".join(results))
