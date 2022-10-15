#!/usr/bin/python3

from logging import exception
from time import sleep

def createDictionary(file):

    dict_aux = {}   #Create Dictinary
    dict_aux1 = {}

    for aux in file:
        aux = aux.split()

        letter = aux[0]
        percentage = float(aux[1])
        
        dict_aux[letter] = percentage

    #Organizing Dict

    for i in sorted(dict_aux, key = dict_aux.get, reverse=True):
        dict_aux1[i] = dict_aux[i]
    
    return dict_aux1

def listFrequency(file):

    aux_int = 0

    #Add in Dict

    for str_Line in file:
        for c in str_Line.upper():
            aux_int += addInDict(c)
    
    #Organizing Dict

    dict_aux = dict()

    for i in sorted(dict_letter, key = dict_letter.get, reverse=True):
        dict_aux[i] = dict_letter[i]

    #Converting to percentage

    for i in dict_aux:
        aux_float = (dict_aux[i] * 100) / aux_int
        dict_aux[i] = round(aux_float, 2)

    return  dict_aux, aux_int   #Dict Organized, Count of letter 
            
def addInDict(c):

    if(ord(c) > 64 and ord(c) < 123):    #Only characters in range 65:122

        if(ord(c) < 91 or ord(c) > 96):

            if (dict_letter.get(c)): # Has in dict
                dict_letter[c] = ((dict_letter.get(c)) + 1)
                        
            else:   #Dont has in dict
                dict_letter[c] = 1  
            
            return 1
    
    return 0    

def findKey(file):

    count_Char = 0

    dict_letter, count_Char = listFrequency(file)

    print(count_Char)

    print(dict_letter)

    print()

    print(dict_language)

    print("END")

#   -------------------- MAIN --------------------   #

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