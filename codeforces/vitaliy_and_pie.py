def min_keys_needed(n, s):
   
    keys = s[::2]  
    doors = s[1::2] 
    
 
    available_keys = set()
    missing_keys = 0
    
   
    for i in range(n - 1):
       
        available_keys.add(keys[i])
        
      
        current_door = doors[i]
        
     
        matching_key = current_door.lower()
        if matching_key not in available_keys:
          
            missing_keys += 1
            available_keys.add(matching_key)
    
    return missing_keys


n = int(input())
s = input().strip()

print(min_keys_needed(n, s))
