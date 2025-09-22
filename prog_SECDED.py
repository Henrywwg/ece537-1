import math

original = [[1, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1]]

for array in original:
    codeword = ""
    #p1, 2
    codeword += str((array[0] + array[1] + array[3])%2)
    codeword += str((array[0] + array[2] + array[3])%2)
    #original data
    codeword += str(array[0])
    #p3
    codeword += str((array[1] + array[2] + array[3])%2)
    #original data
    codeword += str(array[1])
    codeword += str(array[2])
    codeword += str(array[3])

    print(codeword)
