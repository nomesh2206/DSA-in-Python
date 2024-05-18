def toggleTheMiddle(n):
    #Your code here
    binary_str = bin(n)[2:]
    binary_list = list(binary_str)
    length = len(binary_str)
    
    if length % 2 == 0 :
        middle_left_index = length // 2 - 1
        middle_right_index = length // 2
        
        if binary_list[middle_left_index] == "1":
            binary_list[middle_left_index] = "0"
        else:
            binary_list[middle_left_index] = "1"
        
            
        if binary_list[middle_right_index] == "1":
            binary_list[middle_right_index] = "0"
        
        else:
            binary_list[middle_right_index] = "1"
            
    else:
        middle_index = (length + 1) // 2 - 1
        
        if binary_list[middle_index] == "1":
            binary_list[middle_index] = "0"
        
        else:
            binary_list[middle_index] = "1"
        
    new_str = "".join(binary_list)
    
    return int(new_str, 2)
