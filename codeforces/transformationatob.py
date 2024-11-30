def transform(a, b):
    sequence = []
    current = b
    
  
    while current >= a:
        sequence.append(current)
        if current == a:
            break
      
        if current % 2 == 0:
            current //= 2
    
        elif current % 10 == 1:
            current = (current - 1) // 10
        else:
            break
    
  
    if sequence[-1] == a:
        return "YES", len(sequence), sequence[::-1] 
    else:
        return "NO", None, None


a, b = map(int, input().split())


result, length, sequence = transform(a, b)

if result == "YES":
    print(result)
    print(length)
    print(" ".join(map(str, sequence)))
else:
    print(result)
