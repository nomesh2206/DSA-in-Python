class Solution:
 
    #Function to add two matrices.
    def sumMatrix(self,A,B):
        # Check if the dimensions of the matrices are the same.
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return []  # Return None if dimensions don't match.

        # Initialize a result matrix with zeros.
        result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

        # Add corresponding elements of A and B.
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] + B[i][j]

        return result
