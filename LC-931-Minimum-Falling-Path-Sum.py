'''
   Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
   A falling path starts at any element in the first row and chooses the element in the next row that -
   is either directly below or diagonally left/right. Specifically, the next element -
   from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
   
   Example - [[2,1,3],[6,5,4],[7,8,9]]
   output - 13
'''





n = len(A)

for i in range(1, n):
    
    for j in range(n):
        
        mini = math.inf
        for k in range(max(0, j - 1), min(n, j + 2)):
            
            mini = min(mini, A[i - 1][k])
        A[i][j] += mini

print(A[-1])