def find_outlier(arr):
    
    first_three = arr[:3]
    

    even_count = 0
    for num in first_three:
        if num % 2 == 0:
            even_count += 1

  
    if even_count > 1:  
        target_parity = 1  
    else:  
        target_parity = 0  

    
    for num in arr:
        if num % 2 == target_parity:
            return num  


arr = [2, 4, 6, 8, 10, 3]
print(find_outlier(arr)) 
