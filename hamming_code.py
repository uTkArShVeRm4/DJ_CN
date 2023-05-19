def encode(data, parity):

	d7, d6, d5, d3 = [int(bit) for bit in data]

	if parity == 'Even':
		p1 = 1 if (d3+d5+d7)%2 else 0
		p2 = 1 if (d3+d6+d7)%2 else 0
		p4 = 1 if (d5+d6+d7)%2 else 0
	elif parity == 'Odd':
		p1 = 0 if (d3+d5+d7)%2 else 1
		p2 = 0 if (d3+d6+d7)%2 else 1
		p4 = 0 if (d5+d6+d7)%2 else 1

	code = ''.join([str(bit) for bit in [d7,d6,d5,p4,d3,p2,p1]])
	print(f'Hamming code for {data}: {code}')
	return code


def correction(data, parity):
	d7, d6, d5, p4, d3, p2, p1 = [int(bit) for bit in data]

	error = False

	print('Received code: '+data)

	if parity == 'Even':
		if p1 == (d3+d5+d7)%2:
			print('No error at p1 bit')
		else:
			print('Error detected at p1 bit')
			error = True
			p1 = 0 if p1==1 else 1
		if p2 == (d3+d6+d7)%2:
			print('No error at p2 bit')
		else:
			print('Error detected at p2 bit')
			error = True
			p2 = 0 if p2==1 else 1
		if p4 == (d5+d6+d7)%2:
			print('No error at p4 bit')
		else:
			print('Error detected at p4 bit')
			error = True 
			p4 = 0 if p4==1 else 1

	elif parity == 'Odd':
		if p1 != (d3+d5+d7)%2:
			print('No error at p1 bit')
		else:
			print('Error detected at p1 bit')
			error = True
			p1 = 0 if p1==1 else 1
		if p2 != (d3+d6+d7)%2:
			print('No error at p2 bit')
		else:
			print('Error detected at p2 bit')
			error = True
			p2 = 0 if p2==1 else 1
		if p4 != (d5+d6+d7)%2:
			print('No error at p4 bit')
		else:
			print('Error detected at p4 bit')
			error = True
			p4 = 0 if p4==1 else 1	

	if error:
		print("Corrected code: "+''.join([str(bit) for bit in [d7,d6,d5,p4,d3,p2,p1]]))	
	print("Data: "+''.join([str(bit) for bit in [d7,d6,d5,d3]]))				

data = input('Enter 4-bit data: ')
parity = input('Even or Odd parity: ')
code = encode(data,parity)
correction(code,parity)
