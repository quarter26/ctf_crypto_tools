def rot13(plaintext, remove_punc = False):
    ciphertext = ""
    if remove_punc == True:
    	plaintext = plaintext.strip(',', '.', ';','!', '?', '~', '=', '+', '-', '_')
    for i in range(0, len(plaintext)):
        tmp = ord(plaintext[i])
        if 64 < tmp < 91:
        	tmp += 13
        	if tmp > 90:
        		tmp -= 26
        elif 96 < tmp < 123:
        	tmp += 13
        	if tmp > 122:
        		tmp -= 26
        ciphertext += chr(tmp)
    return ciphertext

plaintext = "ABCabc"

print(rot13(plaintext))
