def mergeThree(self, A,B,C):
        #code here
        result = []
        
        # Initialize pointers for A, B, and C
        i, j, k = 0, 0, 0
        
        # Get the lengths of the arrays
        N, M, P = len(A), len(B), len(C)
        
        # Traverse all three arrays and add the smallest element to the result array
        while i < N and j < M and k < P:
            if A[i] <= B[j] and A[i] <= C[k]:
                result.append(A[i])
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                result.append(B[j])
                j += 1
            else:
                result.append(C[k])
                k += 1
        
        # If there are remaining elements in A and B
        while i < N and j < M:
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        
        # If there are remaining elements in B and C
        while j < M and k < P:
            if B[j] <= C[k]:
                result.append(B[j])
                j += 1
            else:
                result.append(C[k])
                k += 1
        
        # If there are remaining elements in A and C
        while i < N and k < P:
            if A[i] <= C[k]:
                result.append(A[i])
                i += 1
            else:
                result.append(C[k])
                k += 1
        
        # Add any remaining elements from A, B, and C
        while i < N:
            result.append(A[i])
            i += 1
        
        while j < M:
            result.append(B[j])
            j += 1
        
        while k < P:
            result.append(C[k])
            k += 1
        
        return result
