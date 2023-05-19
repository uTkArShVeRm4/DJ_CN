def character_count_encode(n):

	stream = ''

	for i in range(n):
		frame = input(f'Enter frame no. {i+1}: ')
		frame = str(len(frame)+1)+frame
		stream += frame

	print('Final stream to be sent = '+stream)	
	return stream


def character_count_decode(stream):

	print('Decoding: '+ stream)

	for i, char in enumerate(stream):
		if char.isdigit():
			print("Frame: "+ stream[i+1:i+1+int(char)-1])


n = int(input('Enter no. of frames: '))

character_count_decode(character_count_encode(n))

