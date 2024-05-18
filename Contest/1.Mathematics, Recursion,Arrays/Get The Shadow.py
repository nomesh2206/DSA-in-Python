class Solution:
    def solve(self, n, a):
        # code here
        sum_n = (n * (n+1))//2
        sum_sqr = ((n * (n+1) * (2*n + 1))//6)
        #sum_arr = sum(a)
        #sum_sqr_arr = 0
        A,B = 0,0
        
        for i in range(n):
            sum_n -= a[i]
            sum_sqr -= a[i]*a[i]
            
        A = (sum_n + sum_sqr//sum_n) // 2
        B = A - sum_n
        
        ans = []
        ans.append(B)
        ans.append(A)
        
        return ans
