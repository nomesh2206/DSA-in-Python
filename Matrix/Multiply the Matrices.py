class Solution:
    
    #Function to multiply two matrices.
    def multiplyMatrix(self,A,B):
        # code here 
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        
        # Check if the matrices can be multiplied.
        if cols_A != rows_B:
            return []
        
        # Initialize the result matrix with zeros.
        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        
        # Multiply the matrices.
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
