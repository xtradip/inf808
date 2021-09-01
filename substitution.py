#coding: utf-8
from ceasar import encrypt
import secrets
from binascii import hexlify
import textwrap

def freq_text(text):
    '''prend un fichier en entree et retourne un dictionnaire avec la frequence pour chaque caracteres associe'''
    # f = open(file,'r')
    d = dict()
    for line in text:
        for c in line:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    # f.close()
    return sorted(d.items(), key= lambda item: item[1], reverse = True)

d = freq_text("text_hugo.txt")
# print(d)

def freq_cipher(file):
    # f = open(file,'rb')
    d = dict()
    with open(file, "rb") as binary_file:
        binary_file.seek(0, 0)  # Go to beginning of the file
        couple_bytes = binary_file.read(2)
        while(couple_bytes):
            if(couple_bytes in d):
                d[couple_bytes] +=1
            else:
                d[couple_bytes] = 1
            couple_bytes = binary_file.read(2)
    # f.close()
    return sorted(d.items(), key= lambda item: item[1], reverse = True) 

print( "*** question 11")
def guess_clear_text( encrypted_text:bytes, decryption_key:dict )  -> str:
    clear_text = ""
    for index in range(len(encrypted_text)):
        if index%2 == 0:
            c = encrypted_text[index:index+2]
            if(c in decryption_key):
                clear_text+=decryption_key[c]
            else:
                # print(str(c))
                clear_text+=str(c)
    return clear_text

def build_decryption_key( freq_clear_text:list, freq_cipher_text:list, key_size:int):
    decryption_key = {}
    for i in range(0,key_size):
        decryption_key[freq_cipher_text[i][0]] = freq_clear_text[i][0]
    return decryption_key

if __name__ == '__main__':
    with open( "cipher_text_1.bin", 'br') as f:
        cipher_text_1_bin = f.read()
    with open( "cipher_text_2.bin", 'br') as f:
        cipher_text_2_bin = f.read()
    cipher_text_1 = "cipher_text_1.bin"
    cipher_text_2 = "cipher_text_2.bin"
    with open( "text_hugo.txt", 'r') as f:
        clear_text_hugo = f.read( )

    print("*** question 8 " ) 
    freq_hugo = freq_text( clear_text_hugo) 
    print( "freq_hugo: %s"%freq_hugo ) 

    print( "*** question 9" )
    freq_cipher_text_1 = freq_cipher(cipher_text_1)
    print(freq_cipher_text_1)
    print( "*** question 11")
    decryption_key = build_decryption_key(  freq_hugo, freq_cipher_text_1, 15 )
    print("decryption_key: %s"%decryption_key)
    clear_text_1 = guess_clear_text( cipher_text_1_bin, decryption_key ) 
    print("clear_text_1: %s"%clear_text_1 )

    # print( "*** question 12" )
    # freq_cipher_text_2 = freq_cipher( cipher_text_2 )
    # decryption_key = build_decryption_key(  freq_hugo, freq_cipher_text_2, key_size=15 )
    # print("decryption_key: %s"%decryption_key)
    # clear_text_2 = guess_clear_text( cipher_text_2_bin, decryption_key ) 
    # print("clear_text_2: %s"%clear_text_2 )

    # print( "*** question 13" )
    # indice = "Anton Voyl n'arrivait pas à dormir"

    # decryption_key = {}
    # for index in range(len(indice)):
    #     bin_char = cipher_text_2_bin[2 * index : 2 * index + 1]
    #     decryption_key[ bin_char ] = indice[ index ]  

    # clear_text_2 = guess_clear_text( cipher_text_2_bin, decryption_key ) 
    # print("clear_text_2: %s"%clear_text_2 )

    # print(freq_cipher("cipher_text_1.bin"))
    # print("#############################################")
    # print(freq_text(clear_text_hugo))