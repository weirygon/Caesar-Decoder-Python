#!/usr/bin/python3

from logging import exception
from time import sleep

def listFrequency(file):

    for str_Line in file:
        for c in str_Line:
            addInDict(c)
            

def addInDict(c):

    if(ord(c) > 64 or ord(c) < 123):    #Only characters in range 65:122

        if (dict_letter.get(c)): # Has in dict
            int_Aux = dict_letter.get(c)
            int_Aux += 1

            dict_letter[c] = int_Aux
                    
        else:   #Dont has in dict
           dict_letter[c] = 1 

def createDictionary(file) :

    dict_aux = {}   #Create Dictinary

    for aux in file:
        aux = aux.split()

        letter = aux[0]
        percentage = float(aux[1])
        
        dict_aux[letter] = percentage
    
    return dict_aux

def findKey(file):

    size_Full = len(file.read())
    file.seek(0)

    listFrequency(file)

    print(dict_letter)

    print("END")

#   ---------- MAIN ----------   #

print(f'{"Caesar Decoder":=^50}')

str_dict_In = "pt.txt"  #input("Inform the name of table frequency: ")

try:
    dict_In = open(str_dict_In, "r")

except FileNotFoundError :
    print("[-] File %s not found!" % (str_dict_In))
    exit()

else:
    print("[+] Opening %s..." % (str_dict_In))

dict_language = createDictionary(dict_In) #Dict with data frequency of language
dict_letter = dict()    #Dict with letter and frequency of text

str_file_In = "teste.txt"   #input("Inform the name of text: ")

try:
    file_In = open(str_file_In)

except FileNotFoundError :
    print("[-] File %s not found!" % (str_file_In))
    exit()

else:
    print("[+] Opening %s..." % (str_file_In))




findKey(file_In)
