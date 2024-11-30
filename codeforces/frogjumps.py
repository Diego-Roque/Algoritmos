def min_d_for_frog(t, test_cases):
    results = []
    for s in test_cases:
        maxL = 0
        currentL = 0
        
     
        for char in s:
            if char == 'L':
                currentL += 1
            else:
                maxL = max(maxL, currentL)
                currentL = 0
        maxL = max(maxL, currentL)  
        
       
        results.append(maxL + 1)
    
    return results


t = int(input())
test_cases = [input().strip() for _ in range(t)]


results = min_d_for_frog(t, test_cases)

for result in results:
    print(result)
