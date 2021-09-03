#coding: utf-8
# from ceasar import encrypt
import secrets
from binascii import hexlify
import textwrap

def freq_text(clear_text:str) ->list:
    '''prend une chaine de caractere en entree et retourne un dictionnaire avec la frequence pour chaque caracteres associe'''
    d = dict()
    for line in clear_text:
        for c in line:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    
    return sorted(d.items(), key= lambda item: item[1], reverse = True)

def freq_cipher(encrypted_text:bytes) ->list:
    # f = open(file,'rb')
    d = dict()
    for index in range(len(encrypted_text)):
        if index%2 == 0:
            c = encrypted_text[index:index+2] 
            if(c in d):
                d[c] += 1
            else:
                # print(str(c))
                d[c] = 1
    return sorted(d.items(), key= lambda item: item[1], reverse = True) 

# print( "*** question 11")
def guess_clear_text( encrypted_text:bytes, decryption_key:dict )  -> str:
    # print(encrypted_text, decryption_key)
    clear_text = ""
    for index in range(len(encrypted_text)):
        if index%2 == 0:
            c = encrypted_text[index:index+2]
            
            if(c in decryption_key):
                clear_text+=decryption_key[c]
            else:
                # print(str(c))
                clear_text+=c.decode("utf-8","ignore")
    return clear_text

def build_decryption_key( freq_clear_text:list, freq_cipher_text:list, key_size:int):
    decryption_key = {}
    for i in range(0,key_size):
        decryption_key[freq_cipher_text[i][0]] = freq_clear_text[i][0]
    return decryption_key

if __name__ == '__main__':
    with open( "cipher_text_1.bin", 'br') as f:
        cipher_text_1 = f.read()
    with open( "cipher_text_2.bin", 'br') as f:
        cipher_text_2 = f.read()
    with open( "text_hugo.txt", 'r') as f:
        clear_text_hugo = f.read( )
    print("*** question 8 " ) 
    freq_hugo = freq_text( clear_text_hugo) 
    print( "freq_hugo: ", freq_hugo ) 
    
    print( "*** question 9" )
    freq_cipher_text_1 = freq_cipher(cipher_text_1)
    print(freq_cipher_text_1)
    print( "*** question 11")
    decryption_key = build_decryption_key(  freq_hugo, freq_cipher_text_1, 15 )
    print("decryption_key: ", decryption_key)
    clear_text_1 = guess_clear_text( cipher_text_1, decryption_key ) 
    print("clear_text_1: ", clear_text_1 )

    print( "*** question 12" )
    freq_cipher_text_2 = freq_cipher( cipher_text_2 )
    decryption_key = build_decryption_key(  freq_hugo, freq_cipher_text_2, key_size=15 )
    print("decryption_key: %s"%decryption_key)
    clear_text_2 = guess_clear_text( cipher_text_2, decryption_key ) 
    print("clear_text_2: %s"%clear_text_2 )

    print( "*** question 13" )
    indice = "Anton Voyl n'arrivait pas à dormir."

    decryption_key = {}
    for index in range(len(indice)):
        bin_char = cipher_text_2[2 * index : 2 * index + 2]
        decryption_key[ bin_char ] = indice[ index ]  

    print(decryption_key)
    clear_text_2 = guess_clear_text( cipher_text_2, decryption_key ) 
    print("clear_text_2: %s"%clear_text_2 )
    freq_clear_text_2 = freq_text(clear_text_2)
    print(freq_clear_text_2)

    # a = [2,3,4,5,6]
    # print(a[0:2])