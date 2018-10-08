# binarystring.py silas
def string_reverse(str1):

	rstr1 = ''
	index = len(str1)
	while index > 0:
		rstr1 += str1[ index - 1 ]
		index = index - 1
	return rstr1

def bincon(decimal):
	print("BINARY\n")
	print(decimal)
	binstr=""
	for i in range (8):
		bin = decimal % 2
		binstr = binstr + str(bin)
		decimal = decimal // 2
		#print (bin)
	revbinstr = string_reverse(binstr)
	print(revbinstr)

def main():
	print("INPUT A 1- TO EXIT THE LOOP")
	print("INPUT A INTEGER LESS THAN 256 AND GREATER THAN -1\n")
	done = 0;
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
		done = dec
main()
