'''
Given an array of integers arr, find the sum of min(b),-
where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.

Example -> arr = [3,1,2,4]
           output = 17
'''

# Solution One

'''-------------------------------------------------------------------------------------'''

arr = [3,1,2,4]

ans , n , prev = 0 ,len(arr) ,0

for i in range(n):
    
    prev = arr[i]
    
    for j in range(i+1,n):
        
        if arr[j] < prev:
            
            prev = arr[j]
            
        ans += prev
        
        
print(ans)

'''--------------------------------------------------------------------------------------'''

# Solution Two


res = 0
    
stack = []

for i, n in enumerate(arr):
    
    while stack and n < stack[-1][1]:
        j,m  = stack.pop()
        
        left = j - stack[-1][0] if stack else j + 1
        right = i - j
        
        res = (res + m*left*right)%mod
        
    stack.append((i,n))
            
for i in range(len(stack)):
    
    j,n = stack[i]
    
    left= j - stack[i-1][0] if i >0 else j + 1
    
    right = len(arr) - j
    
    res = (res + n*left*right)%mod
    
print(res)