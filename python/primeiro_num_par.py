def primeiro_num_par(array):
    for k in range(len(array)):
        if( array[k] % 2 == 0 ):
            return k
        
    return 0

ar= [1,2, 3, 4, 5, 6, 7, 8]

print("o primeiro numero par do array é : ", ar[primeiro_num_par(ar)])