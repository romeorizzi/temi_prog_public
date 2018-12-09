"""
* user:  VR422153
* fname: ELEONORA
* lname: GIACOMELLI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:43:17.698752
"""

a, b, c = map(int, input().split())

def conta_multipli(a, b, c): 
    sol=0
    i=1
    m=0
    if m<=b:
        while ((a*i)<=c):
            if (a*i)%b !=0:
                sol +=1
            i +=1
    else:
        b +=b        
    return sol
                
print(conta_multipli(a, b, c))
