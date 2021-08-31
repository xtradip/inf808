#coding: utf-8

def translation_char(c, k):
    # t est la translation de char + k
    if(ord(c) >= 97 and ord(c) <= 122): #majuscule
        return chr(((ord(c) + k - 97) % 26 + 97))
    elif(ord(c) >= 65 and ord(c) <= 90):#minuscule
        return chr(((ord(c) + k-65) % 26 + 65))
    else:
        return 0

def encrypt(str, k):
    caesar = ""
    #encrypte le message en utilisant la translation de char de caesar
    for c in str:
        caesar += translation_char(c,k)
    
    return caesar

def decrypt(str,k):
    return encrypt(str, (26-k)%26)

print(translation_char('A',26))
k = 100
a = encrypt("abcde", k)

print(decrypt(a, k))



