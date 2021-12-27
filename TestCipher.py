#  File: TestCipher.py

#  Description: Program encodes and decodes input string through railfence or vigenere

import sys

def rail_fence_encode ( strng, key ):
    rail_fence = [['' for i in range(len(strng))] for i in range(key)]
    col = 0
    row = 0
    up_down = 1
    rail_fence_encode = ''
    for letter in strng:
        if row + up_down < 0 or row + up_down >= key:
            up_down = up_down * -1 # program will change direction
        rail_fence[row][col] = letter
        row += up_down
        col += 1

    for rail in rail_fence:
        rail_fence_encode += ''.join(rail)
    return rail_fence_encode

def rail_fence_decode ( strng, key ):
    rail_fence = [['' for i in range(len(strng))] for i in range(key)]
    col = 0
    row = 0
    up_down = 1
    rail_fence_encode = ''
    for i in range(len(strng)):
        if row + up_down < 0 or row + up_down >= key:
            up_down = up_down * -1 # program will change direction
        rail_fence[row][col] = 0
        row += up_down
        col += 1

    strng_index = 0
    row = -1
    for rail in range(0, len(rail_fence)):
        row += 1
        col = -1
        selected_rail = rail_fence[rail]
        for position in range(0, len(selected_rail)):
            col += 1
            if selected_rail[position] == 0:
                rail_fence[row][col]=strng[strng_index]
                strng_index += 1

    flipped_rail_fence = [[row[i] for row in rail_fence] for i in range(len(rail_fence[0]))]

    for flipped_rail in flipped_rail_fence:
        rail_fence_encode += ''.join(flipped_rail)
    return rail_fence_encode

def filter_string ( strng ):
    for c in strng:
        if c.isalpha() is False:
            strng = strng.replace(c,"")
    clean_string = strng.lower()
    return clean_string

#returns the userString under the pass phrase - e.g. helloworld -> sealsealse
def passPhrase(userString, key): 
    temp = key

    #if pass phrase matches length of string return
    if len(userString) == len(key): 
        return key

        #when pass phrase doesn't match length of string
    for i in range(len(userString) - len(key)): 
        temp += (key[i % len(key)]) 
    return temp

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
    x = (ord(p) + ord(s) - 194) % 26

    #returning to ascii values
    x += ord('a')
    return chr(x)

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    x = (ord(s) - ord(p)) % 26

    #return to ascii values
    x += ord('a')

    return chr(x)

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    convertedText = passPhrase(strng, phrase)
    encryptedText = ""

    for i in range(len(strng)): 
        #formula is position of alphabet combined together
        encryptedText += encode_character(convertedText[i], strng[i])

    return encryptedText

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    convertedText = passPhrase(strng, phrase)
    decryptedText = ""

    for i in range(len(strng)): 
        decryptedText += decode_character(convertedText[i], strng[i])

    return decryptedText
    
def main():
    print("Rail Fence Cipher")
    rail_fence_plain = sys.stdin.readline().strip()
    rail_fence_key = int(sys.stdin.readline())
    print("")
    print("Plain Text:", rail_fence_plain)
    print("Key:", rail_fence_key)
    print("Encoded Text:", rail_fence_encode ( rail_fence_plain, rail_fence_key ))
    print("")
    
    rail_fence_encoded = sys.stdin.readline().strip()
    rail_fence_encoded_key = int(sys.stdin.readline())
    print("Encoded Text:", rail_fence_encoded)
    print("Enter Key:", rail_fence_encoded_key)
    print("Decoded Text:", rail_fence_decode ( rail_fence_encoded, rail_fence_encoded_key ))
    print("")

    print("Vigenere Cipher")
    vigenere_plain = filter_string(sys.stdin.readline().strip())
    vigenere_pass = sys.stdin.readline().strip()
    print("")
    print("Plain Text:", vigenere_plain)
    print("Pass Phrase:", vigenere_pass)
    print("Encoded Text:", vigenere_encode( vigenere_plain, vigenere_pass ))
    print("")
    print("Encoded Text:", vigenere_encode ( vigenere_plain, vigenere_pass ))
    print("Pass Phrase:", vigenere_pass)
    print("Decoded Text:", vigenere_decode ( vigenere_encode( vigenere_plain, vigenere_pass ), vigenere_pass ))
    
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  #main()
  print(decode_character('s', 'b'))
  print(vigenere_decode('zilwgaocdh', 'seal'))
