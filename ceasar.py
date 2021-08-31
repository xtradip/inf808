#coding: utf-8

def translation_char(c, k):
    # t est la translation de char + k
    if(ord(c) >= 97 and ord(c) <= 122):
        t = ((ord(c) + k - 97) % 26 + 97)
        
        return chr(t)
    else:
        return 0

print(translation_char('a',26))