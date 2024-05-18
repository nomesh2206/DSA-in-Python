def FindMaxSum(arr,n):
    #Your code here
    include = 0
    exclude = 0
    
    for i in arr:
        if exclude > include:
            exclude_new = exclude
            
        else :
            exclude_new = include
        
        include = exclude + int(i)
        exclude = exclude_new
        
    if exclude > include:
        return exclude
    else:
        return include
