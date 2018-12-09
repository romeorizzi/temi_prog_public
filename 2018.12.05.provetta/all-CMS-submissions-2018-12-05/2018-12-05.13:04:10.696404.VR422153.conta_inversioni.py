"""
* user:  VR422153
* fname: ELEONORA
* lname: GIACOMELLI
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 13:04:10.696404
"""
p = list(map(int, input().strip().split()))




#from __future__ import print_function
#import sys

def numero_di_inversioni(p):
    
    for i in range (0, len(p)): 
        if p[0]>p[1]:
            i +=1
            return i
   #for i in range (1, len(p)):
        if p[2]>p[3]:
            i +=1
             return i
p=i+n
#rint(n+i)

        
    #return 42

#if sys.version_info < (3, 0):
    #input = raw_input # in python2, l'equivalente di input è raw_input


print(numero_di_inversioni(p))
