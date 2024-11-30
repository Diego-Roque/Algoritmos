def can_reach_end(n, row1, row2):
   
    for i in range(n):
        if row1[i] == row2[i]: 
            continue
        else:
            return "NO"
    return "YES"


t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    row1 = input().strip()
    row2 = input().strip()
    results.append(can_reach_end(n, row1, row2))


print("\n".join(results))
