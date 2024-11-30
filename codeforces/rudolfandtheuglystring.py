def min_deletions_to_beautiful(s):
    n = len(s)
    
  
    bad_substrings = ["pie", "map"]
    
   
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
      
        dp[i] = dp[i-1] + 1
        
      
        for j in range(max(0, i-3), i):
         
            curr_substr = s[j:i]
            
            if curr_substr in bad_substrings:
                continue
            
         
            dp[i] = min(dp[i], dp[j] + (i-j-len(curr_substr)))
    
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    print(min_deletions_to_beautiful(s))
