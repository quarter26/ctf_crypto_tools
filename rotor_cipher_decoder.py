def rotor_cipher(rotor, cipher, key):
    tmp_list=[]
    for i in range(0, len(rotor)):
        tmp=""
        k = key[i] - 1
        for j in range(0, len(rotor[k])):
            if cipher[i] == rotor[k][j]:
                if j == 0:
                    tmp=rotor[k]
                    break
                else:
                    tmp=rotor[k][j:] + rotor[k][0:j]
                    break
        tmp_list.append(tmp)
    message_list = []
    for i in range(0, len(tmp_list[i])):
        tmp = ""
        for j in range(0, len(tmp_list)):
            tmp += tmp_list[j][i]
        message_list.append(tmp)

    return message_list


rotor = [
    "ZWAXJGDLUBVIQHKYPNTCRMOSFE", "KPBELNACZDTRXMJQOYHGVSFUWI", 
    "BDMAIZVRNSJUWFHTEQGYXPLOCK", "RPLNDVHGFCUKTEBSXQYIZMJWAO", 
    "IHFRLABEUOTSGJVDKCPMNZQWXY", "AMKGHIWPNYCJBFZDRUSLOQXVET", 
    "GWTHSPYBXIZULVKMRAFDCEONJQ", "NOZUTWDCVRJLXKISEFAPMYGHBQ", 
    "XPLTDSRFHENYVUBMCQWAOIKZGJ", "UDNAJFBOWTGVRSCZQKELMXYIHP", 
    "MNBVCXZQWERTPOIUYALSKDJFHG", "LVNCMXZPQOWEIURYTASBKJDFHG", 
    "JZQAWSXCDERFVBGTYHNUMKILOP" 
]

cipher = "NFQKSEVOQOFNP"

key = [2,3,7,5,13,12,9,1,8,10,4,11,6]

print(rotor_cipher(rotor, cipher, key))
