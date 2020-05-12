def rot13_1(plaintext, remove_punc = False):
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


def rot13_2(text, isEncrypt):
    alphabet = u"abcdefghijklmnopqrstuvwxyz"
    ans = ''
    key = len(alphabet) >> 1
    # if number letters in the alphabet is odd
    if len(alphabet) & 1:
        alphabet += alphabet[key]
        key += 1
    
    for char in text.lower():
        try:
            alphIndex = alphabet.index(char)
        except ValueError as e:
            wrchar = char.encode('utf-8')
            e.args = (
                "Can't find char '" + wrchar + "' of text in alphabet!",)
            raise
        alphIndex = (alphIndex + isEncrypt * key) % len(alphabet)
        ans += alphabet[alphIndex]
    return ans

'''
file_handle1=open('gogogo.pdf','rb+')
file_handle2=open('new.pdf','wb')

lines = file_handle1.readlines()
for line in lines:
    for i in line:
        if 64 < i < 91:
            i += 13
            if i > 90:
                i -= 26
        elif 96 < i < 123:
            i += 13
            if i > 122:
                i -= 26
        i = i.to_bytes(1, 'little')
        file_handle2.write(i)
print('done')
'''

file_handle1.close()
file_handle2.close()



plaintext = "ABCabc"

print(rot13_1(plaintext))

print(rot13_2(plaintext))
