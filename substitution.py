#coding: utf-8
import binascii

def freq_text(file):
    '''prend un fichier en entree et retourne un dictionnaire avec la frequence pour chaque caracteres associe'''
    f = open(file,'r')
    d = dict()
    for line in f:
        for c in line:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    f.close()
    return sorted(d.items(), key= lambda item: item[1], reverse = True)

d = freq_text("text_hugo.txt")
# print(d)

def freq_cipher(file):
    f = open(file,'rb')
    d = dict()
    with open(file, "rb") as binary_file:
    # Seek a specific position in the file and read N bytes
        binary_file.seek(0, 0)  # Go to beginning of the file
        couple_bytes = binary_file.read(2)
        while(couple_bytes):
            if(couple_bytes in d):
                d[couple_bytes] +=1
            else:
                d[couple_bytes] = 1
            couple_bytes = binary_file.read(2)
    f.close()
    return sorted(d.items(), key= lambda item: item[1], reverse = True) 


print(freq_cipher("cipher_text_1.bin"))
