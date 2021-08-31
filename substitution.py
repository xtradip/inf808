#coding: utf-8

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
    return sorted(d.items(), key= lambda item: item[1], reverse = True)

print(freq_text("test.txt"))