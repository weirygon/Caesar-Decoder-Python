#!/bin/python3

from logging import exception

def createDictionary(file) :

    dict_aux = {}   #Create Dictinary

    for aux in file:
        aux = aux.split()

        letter = aux[0]
        percentage = float(aux[1])
        
        dict_aux[letter] = percentage
    
    return dict_aux

#   ---------- MAIN ----------   #

print(f'{"Caesar Decoder":=^50}')

str_file_In = input("Inform name of table frequency: ")

try:
    file_In = open(str_file_In, "r")

except FileNotFoundError :
    print("[-] File %s not found!" % (str_file_In))
    exit()

else:
    print("[+] Opening %s..." % (str_file_In))

dict_language = createDictionary(file_In)

print(dict_language)