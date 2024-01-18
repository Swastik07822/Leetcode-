'''
  You are climbing a staircase. It takes n steps to reach the top.
  Each time you can either climb 1 or 2 steps.
  In how many distinct ways can you climb to the top?
  
  n = 5 
  output = 8
  
  Explanation -> (1,1,1,1,1) , (1,2,1,1) , (2,1,1,1) ,(1,1,2,1) , (1,1,1,2) ,
           (2,2,1) ,(1,2,1) ,(1,2,2)
           
    
         
'''

# Recursive approach

n = 5

dp = [-1 for _ in range(n+1)]
        
def climb(step):
            
    if step == 0: return 1
    
    if step <0: return 0
    
    if dp[step] != -1: return dp[step]

    one_step =  climb(step-1)
    
    two_step = climb(step-2)
    
    dp[step] = one_step + two_step
    
    return dp[step]
        
return climb(n)


# Itertive approach using dynammic programming

dp = [0 for _ in range(n+1)]

dp[0],dp[1] = 1,1

if n == 1: return 1

if n == 2: return dp[0] + dp[1]

for i in range(2,n+1):
    
    dp[i] = dp[i-1] + dp[i-2]
    
return dp[n]