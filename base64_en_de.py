import base64

base64encode = lambda encodestr: str(base64.b64encode(encodestr.encode('utf-8')), 'utf-8')

base64decode = lambda decodestr: str(base64.b64decode(decodestr.encode('utf-8')), 'utf-8')

tmp = 'Base64 Encode Test gogogo'
tmp_e = base64encode(tmp)
tmp_d = base64decode(tmp_e)

print(tmp_e)
print(tmp_d)

if tmp == tmp_d:
	print(True)
