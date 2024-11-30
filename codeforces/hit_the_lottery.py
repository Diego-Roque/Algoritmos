def minimum_bills(n):
  
    denominations = [100, 20, 10, 5, 1]
    count = 0
    
    for bill in denominations:
        count += n // bill  
        n %= bill           
    
    return count

n = int(input().strip())
print(minimum_bills(n))
