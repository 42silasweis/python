#hexdec.py silas
def bincon(decimal):
    bin_str = ""
    for i in range(8):
        binary = str(decimal % 2)
        decimal = decimal // 2
        bin_str = bin_str + str(binary)
        if(i == 3):
            bin_str = bin_str + " "
    return bin_str[::-1]

def hexcon(decimal):
    hex_str = ""
    #remainder = str (decimal % 16)
    if (decimal % 16 > 9):
        addasc = 55
    else:
        addasc = 48
    remainder = str(chr((decimal % 16)+addasc))
    # **********************************
    if (decimal // 16 > 9):
        addasc = 55
    else:
        addasc = 48
    quotient = str(chr((decimal // 16)+addasc))
    hex_str = quotient+remainder
    # **********************************
    return hex_str

def main():
    dec = 0;
    while (dec < 256):
        hexs = hexcon(dec)
        bins = bincon(dec)
        print(dec,hexs,bins)
        dec +=1
main()
