import math

original = [[1, 1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1]]

for array in original:
    cw = ""
    for val in array:
        cw += str(val)
        
    data_nibble = str(array[2]) + str(array[4]) + str(array[5]) + str(array[6])
        
    rx_syndrome = ""
    tx_syndrome = str(array[0]) + str(array[1]) + str(array[3]) 
    #Generate syndrome
    rx_syndrome += str((array[3] + array[4] + array[5] + array[6] )%2)  #C4
    rx_syndrome += str((array[1] + array[2] + array[5] + array[6] )%2)  #C2
    rx_syndrome += str((array[0] + array[2] + array[4] + array[6] )%2)  #C1

    print("Syndrome: " + rx_syndrome)
    
    if rx_syndrome == "000":
        print("No error")
        print("Correct codeword is: " + cw)
        print("Original nibble: " + data_nibble)
    
    else:
        bitpos = 0
        if rx_syndrome[0] == '1':
            bitpos += 4
        if rx_syndrome[1] == '1':
            bitpos += 2
        if rx_syndrome[2] == '1':
            bitpos += 1 
            
        print("Error at bit " + str(bitpos))
        
        #correct codeword
        if cw[bitpos - 1] == '1':
            cw = cw[0:bitpos-1] + '0' + cw[bitpos :]
        else:
            cw = cw[0:bitpos-1] + '1' + cw[bitpos :]
        
        data_nibble = cw[2] + cw[4] + cw[5] + cw[6]
        print("Correct codeword: " + cw)
        print("Original nibble: " + data_nibble)

    print()

    