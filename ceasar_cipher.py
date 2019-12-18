def ceasar_enc(plaintext, key = 1, loop = False):
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(0, len(plaintext)):
        tmp = ord(plaintext[i]) + key
        if (loop == True):
            if tmp > 90:
                tmp -= 26
        ciphertext += chr(tmp)
    return ciphertext

def ceasar_dec(ciphertext, key = 1, loop = False):
    ciphertext = ciphertext.upper()
    plaintext = ""
    for i in range(0, len(ciphertext)):
        tmp = ord(ciphertext[i]) - key
        if (loop == True):
            if tmp < 65:
                tmp += 26
        plaintext += chr(tmp)
    return plaintext

plaintext = "WXy"
ciphertext = "BCDE"

print(ceasar_enc(plaintext))
print(ceasar_enc(plaintext, 4, True))
print(ceasar_dec(ciphertext, 3))
print(ceasar_dec(ciphertext, 3, True))
