import math
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
  def decimalToBinary(decimal):
    binary=[]
    while decimal >= 1:
        
        binary.append(decimal%2)
        
        decimal = decimal/2
    i=0
    for number in binary:
        binary[i]=str(int(math.trunc(binary[i])))
        
        i+=1
    final = "".join(binary[::-1])
    
    while len(final)<8:
      #im not sure if this is good practice but it works
            final =final[::-1]
            final=final+"0"
            final =final[::-1]
   
    return(final)
def decodeBase64():
    base64_characters = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
    'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51,
    '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63
}
    #file = open(fr"C:\Users\starw\Desktop\Siyools\Python tools\crypto.txt","r")
    plainText = input("What do you want to decode? \n")
    combined=""
    nums = []
    ascii = []
    final=""
    for char in plainText:
        #print(base64_characters[char])
        nums.append(decimalToBinary(base64_characters[char])[2:])
    combined="".join(nums)
    print(nums)
    print(combined)
    while len(combined)>0:

        
        ascii.append(combined[:8])
        combined=combined[8:]
    for char in ascii:
        char = binaryToDecimal(char)
        
        final+= chr(char)
    
    print(final)
base64decode()
