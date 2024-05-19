def pairExists(arr,n,c):
    #Your code here

    s=set(arr)  # since we dont need the order of elements here
    '''
    OR
    s = set()  # if we want to maintain the order of elements in arr 
    for i in range(n):
        if arr[i] not in s:
            s.add(arr[i])
    '''
    
    for i in range(n):
        if arr[i]^c in s:
            return True
    
    return False
