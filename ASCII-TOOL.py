from colorama import init, Fore, Back, Style

def banner():
	print('				+----------+')
	print('				|ASCII-TOOL|')
	print('				+----------+')
	print('								,,,,,,,,,,,,,,,')
	print('								|made by okt4v|')
	print("								'''''''''''''''")
	print('\n')

def textToAscii():
	print('\n')
	print('Text to ASCII selected ')

	while True:
		print('Enter the filepath to your file you would like to convert')
		print('   | ')
		tfilepath = input('   +--» ')		

		if not tfilepath.endswith('.txt'):
			print('The file needs to be a .txt file ')
			continue

		try:
			with open(tfilepath, 'r') as file:
				content = file.read()
				file.close()
			break
		except FileNotFoundError:
			print('File not found error ')
		except:
			print('An error has occured ')

	while True:		
		print('Enter the filepath for the output file ')
		print('   | ')
		wfilepath = input('   +--» ')
		wfilename = wfilepath.split('/')[-1]
		if not wfilename.endswith('.txt'):
			print('The file needs to be a .txt file ')
		else:
			break
	print(f'The output file {wfilename} has been sucsessfuly created ')


	asciicontent = ''
	for char in content:
		ascchar = str(ord(char))
		asciicontent += ascchar 
		asciicontent += ' '

	with open(wfilepath, 'w') as file:
		file.write(asciicontent)
		file.write('\n')
		file.close()

def asciiToText():
	print('\n')
	print('ASCII to Text selected ')

	while True:
		print('Enter the filepath to your file you would like to convert')
		print('   | ')
		tfilepath = input('   +--» ')		

		if not tfilepath.endswith('.txt'):
			print('The file needs to be a .txt file ')
			continue

		try:
			with open(tfilepath, 'r') as file:
				content = file.read()
				file.close()
			break
		except FileNotFoundError:
			print('File not found error ')
		except:
			print('An error has occured ')

	while True:		
		print('Enter the filepath for the output file ')
		print('   | ')
		wfilepath = input('   +--» ')
		wfilename = wfilepath.split('/')[-1]
		if not wfilename.endswith('.txt'):
			print('The file needs to be a .txt file ')
		else:
			break
	print(f'The output file {wfilename} has been sucsessfuly created ')

	textcontent = ''
	temp = ''
	for achar in content:
		if not achar == ' ':
			temp += achar 
		elif achar == ' ':
			converted = chr(int(temp))
			textcontent += str(converted)
			temp = ''
			continue

	with open(wfilepath, 'w') as file:
		file.write(textcontent)
		file.write('\n')
		file.close()

def selectAndStart():
	print('[1] for text to ASCII ')
	print('[2] for ASCII to text ')
	while True:
		print('   | ')
		selected = input('   +--» ')
		if selected == '1':
			textToAscii()
			break

		if selected == '2':
			asciiToText()
			break

		else:
			print('Enter a valid input ')







def main():
	banner()
	selectAndStart()


main()	