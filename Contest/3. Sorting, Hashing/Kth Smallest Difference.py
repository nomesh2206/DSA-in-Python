def kthDiff(a, n, k):
    #Your code here
    a.sort()
    small = 0
    large = a[n-1] - a[0]
    
    while small < large:
        middle = (small+large) // 2
        count = 0 
        left = 0
        
        for right in range(n):
            while a[right] - a[left] > middle:
                left += 1
            count += right-left
            
        if count >= k:
            large = middle
                
        else:
            small = middle + 1
                
    return small
