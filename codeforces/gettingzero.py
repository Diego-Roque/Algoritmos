def min_operations_to_zero(n, a):
    MOD = 32768
    results = []
    
    for v in a:
        min_ops = float('inf')
        
     
        for increments in range(16):
          
            new_value = (v + increments) % MOD
    
            doublings = 0
            while new_value > 0:
                new_value = (2 * new_value) % MOD
                doublings += 1
        
            min_ops = min(min_ops, increments + doublings)
        
        results.append(min_ops)
    
    return results


n = int(input().strip())
a = list(map(int, input().strip().split()))


result = min_operations_to_zero(n, a)


print(" ".join(map(str, result)))
