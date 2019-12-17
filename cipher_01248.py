def cipher01248(ciphertext):
    ''' 01248 cipher '''
    
    # Split ciphertext with 0, return a list
    ciphertext = ciphertext.split("0")  
    
    # define a void message
    plaintext = ""  # 定义一个空的明文

    # Since every element is a letter
    for i in range(0, len(ciphertext)):
        sub_sum = 0
        # For every digit of element in c(every element is str type)
        for j in range(0, len(ciphertext[i])):
            # Sum up all digits in sub-element
            sub_sum += int(ciphertext[i][j])
        # ASCII convert.
        plaintext += chr(sub_sum + 64)
    return plaintext


c = "8842101220480224404014224202480122"
print(cipher01248(c))
