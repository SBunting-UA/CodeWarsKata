def count_bits(n):
    n_bin = bin(n)[2:]
    check = []
    counter = 0
    
    for val in n_bin:
        check.append(val)
        
    for val in check:
        if int(val) == 1:
            counter += 1
            
    return counter
