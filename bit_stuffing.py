def encode(stream):

	binary = ''.join(format(ord(n),'b') for n in stream)
	print(f"{stream} in binary = {binary}")
	print('Stuffing bits')
	for i,bit in enumerate(binary):
		if('11111' ==  binary[i:i+5]):
			binary = binary[:i+5]+'0'+binary[i+5:]		
	binary = '01111110'+binary+'01111110'
	print(binary)
	return binary

def decode(binary):
	print('unstuffing bits')
	stream = binary[8:-8]
	for i,bit in enumerate(stream):
		if(stream[i:i+5]=='11111'):
			stream = stream[:i+5]+stream[i+6:]
	print(stream)
	out = ''
	for i in range(0,len(stream),7):
		out += chr(int(stream[i:i+7],2))

	print(out)	

	


decode(encode(input('Enter string: ')))