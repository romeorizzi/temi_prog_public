"""
* user:  VR429669
* fname: DAVIDE
* lname: CAMPONOGARA
* task:  rank_unrank_ABstrings
* score: 50.0
* date:  2018-12-05 12:48:25.852761
"""
#!/usr/bin/env python3
# -*- coding: latin-1 -*-

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input # in python2, l'equivalente di input è raw_input


# Template di soluzione per il problema rank_unrank_ABstrings

def ABstring2rank(s):
    alfabeto=["A","B"]
    #for c in s:
    #    if(c not in alfabeto):
    #        alfabeto+=[c]
    #ordinato=ordina(alfabeto)
    ordinato=alfabeto    
    soluzione=0
    for i in range(0,len(s)):
        soluzione+=indexof(ordinato,s[len(s)-1-i])*(len(ordinato)**i)    
    return soluzione

def ABstring_of_len_and_rank(length, r):
    parola=""  
    while(r!=0):
        print(r%2)
        if(r%2==0):
            parola="A"+parola
        else:
            parola="B"+parola
        r=int(r/2)
    if(len(parola)<length):
        parola="A"*(length-len(parola))+parola
    return parola   

def indexof(lista,elemento):
    i=0
    while(lista[i]!=elemento):
        i+=1
    return i     

def trovaMin(lista):
    i=0
    found=False
    while (i<len(lista) and not found):
        c=lista[i]        
        found=True
        for a in lista:
            if(ord(c)>ord(a)):
                found=False
        i+=1
    return c
def ordina(lista):
    lunghezza=len(lista)
    ordinata=[]
    i=0
    while(i< lunghezza):
        el=trovaMin(lista)
        ordinata+=[el]
        lista=lista[0:indexof(lista,el)]+lista[indexof(lista,el)+1:]
        i+=1
    return ordinata

input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print( ABstring2rank(input_string) )
else:
   length, r = input_string.split()
   print( ABstring_of_len_and_rank(int(length), int(r)) )


