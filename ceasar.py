#coding: utf-8

def translation_char(c, k):
    # t est la translation de char + k
    if(ord(c) >= 97 and ord(c) <= 122): #majuscule
        return chr(((ord(c) + k - 97) % 26 + 97))
    elif(ord(c) >= 65 and ord(c) <= 90):#minuscule
        return chr(((ord(c) + k-65) % 26 + 65))
    else:
        return c

def encrypt(str, k):
    caesar = ""
    #encrypte le message en utilisant la translation de char de caesar
    for c in str:
        caesar += translation_char(c,k)
    
    return caesar

def decrypt(str,k):
    return encrypt(str, (26-k)%26)


def force_brute(str):
    d = {}
    x = 1
    while(x != 26):
        d[x] = decrypt(str,x)
        x+=1
    return d

def check_force_brute(d, str):
    # d est un dict avec la force brute, str est le message original
    # fonction qui permet de checker si il existe le message original dans d 
    # retourne True avec la cle qui permet de dechiffrer
    for k_test in d:
        # print(d[k_test])
        if(d[k_test] == str):
            return True, k_test
    return False

print(translation_char('A',26))
k = 100
m = "yes it was the right thing"
print("###### Q2 ######")
a = encrypt(m, k)
print(a)
#Q3
print("###### Q3 ######")
print(encrypt(decrypt("abcde", k),k))
print("###### Q4 ######")
d = force_brute(a)
check, k_trouve = check_force_brute(d, m)
print(decrypt(a,k_trouve))


