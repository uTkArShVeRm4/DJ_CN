def convert_to_binary(stream):
	binary = ''.join(format(ord(n),'b') for n in stream)
	print(f"{stream} in binary = {binary}")
	return binary

def convert_to_string(binary):
	out = ''
	for i in range(0,len(binary),7):
		out += chr(int(binary[i:i+7],2))

	print(out)	
	return out

def encode(binary):
	ESC = '01010101'
	FLAG = '01111110'
	for i in range(0,len(binary),7):
		if(FLAG ==  binary[i:i+8] or ESC == binary[i:i+8]):
			binary = binary[:i]+ESC+binary[i:]
	binary = FLAG+binary+FLAG
	print('After byte stuffing: \n'+binary)
	return binary		

def decode(binary):
	ESC = '01010101'
	FLAG = '01111110'
	binary = binary[8:-8]
	for i in range(0,len(binary),7):
		if(ESC ==  binary[i:i+8]):
			binary = binary[:i]+binary[i+8:]
	print('After byte destuffing: \n'+binary)
	return binary		

print('ESC: 01010101')
print('FLAG: 01111110')	
stream = input('Enter string to send: ')

binary = encode(convert_to_binary(stream))

stream = convert_to_string(decode(binary))