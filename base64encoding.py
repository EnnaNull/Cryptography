def binaryToDecimal(binary):
        decimals = []
        place = 0
        finalInt = 0
        binary = list(binary)
        for i in range(len(binary)):
            
            tempInt = int(binary[-1]) * (2**place)
           
            binary.pop(-1)
            decimals.append(tempInt)
            place+=1 
            
        for number in decimals:
            finalInt = finalInt + number
        return(finalInt)
def base64():
    base64_characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]
    file = open(fr"C:\Users\starw\Desktop\Siyools\Python tools\crypto.txt","r")
    plainText = file.read()
    combined=""
    chunks = []
    for char in plainText:
        ascii = ord(char)
        print(char,ascii)
        binary = format(ascii,'08b')
        #this was a bad idea
        #binary=binary.replace("0b","")
        
        combined+=binary
    #still dont need this
   # while len(combined)%3!=0:
    #    combined+="="
    print(combined)
    while len(combined)>0:

        
        chunks.append(combined[:6])
        combined=combined[6:]
    
    while len(chunks[-1])<6:
        chunks[-1]+="0"
    
    i=0
    for chunk in chunks:
        
        chunks[i]=binaryToDecimal(chunk)
        
        chunks[i]=base64_characters[chunks[i]]
        i+=1
    base64encoding = "".join(chunks)
    print(base64encoding)
