"""
* user:  VR422153
* fname: ELEONORA
* lname: GIACOMELLI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:28:06.906365
"""
p = list(map(int, input().strip().split()))




#from __future__ import print_function
#import sys

def numero_di_inversioni(p):
    inv = 0
    for i in range (0, len(p)): 
        
        for j in range (i+1, len(p)):
             if(p[i]>p[j]):
                 inv +=1
             
#=i+
#rint(n+i)

        
    return inv

#if sys.version_info < (3, 0):
    #input = raw_input # in python2, l'equivalente di input è raw_input


print(numero_di_inversioni(p))
