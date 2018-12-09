"""
* user:  VR437151
* fname: GIACOMO
* lname: BARTOLI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:38:33.082846
"""
#!/usr/bin/env python3
def conta_multipli(a, b, c):
    n = 0   
    for i in range (c+1):
        if i%a == 0:
            n = n+1
        if i%b == 0 and i%a == 0:
            n = n-1     
    return(n)
    
# Lettura input: non devi modificare il codice sotto questa riga
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
