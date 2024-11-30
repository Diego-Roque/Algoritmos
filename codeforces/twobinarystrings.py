def can_transform(a, b):
  
    if a == b:
        return "YES"
    
 
    if len(a) != len(b) or a[0] != '0' or a[-1] != '1' or b[0] != '0' or b[-1] != '1':
        return "NO"
    
 
    if a.count('0') != b.count('0') or a.count('1') != b.count('1'):
        return "NO"
    
  
    return "YES"

t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    
  
    print(can_transform(a, b))
