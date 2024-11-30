def can_transform_to_2020(s):
   
    if s == "2020":
        return True
    
    n = len(s)
    
   
    if "2020" in s:
        return True
    
   
    for i in range(n):
        for j in range(i, n):
          
            new_s = s[:i] + s[j+1:]
         
            if new_s == "2020":
                return True
            
       
            if "2020" in new_s:
                return True
    
    return False

def main():
 
    t = int(input())
    
  
    for _ in range(t):
      
        n = int(input())
        s = input().strip()
        
      
        print("YES" if can_transform_to_2020(s) else "NO")

if __name__ == "__main__":
    main()
