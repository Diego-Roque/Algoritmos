def solve_test_case(n, arr):
  ty
    dp_even = [float('-inf')] * n 
    dp_odd = [float('-inf')] * n   

  
    if arr[0] % 2 == 0:
        dp_even[0] = arr[0]
    else:
        dp_odd[0] = arr[0]

  
    max_sum = arr[0]

 
    for i in range(1, n):
        if arr[i] % 2 == 0:  
            dp_even[i] = max(arr[i], dp_odd[i-1] + arr[i])
            

            max_sum = max(max_sum, dp_even[i])
        else: 
            dp_odd[i] = max(arr[i], dp_even[i-1] + arr[i])
            
          
            max_sum = max(max_sum, dp_odd[i])

    return max_sum

def main():
  
    t = int(input())

 
    for _ in range(t):
     
        n = int(input())
        arr = list(map(int, input().split()))
        
     
        print(solve_test_case(n, arr))


if __name__ == "__main__":
    main()
