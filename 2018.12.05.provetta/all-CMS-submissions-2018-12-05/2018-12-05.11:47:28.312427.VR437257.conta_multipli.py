"""
* user:  VR437257
* fname: BENEDETTA
* lname: TOMMASI
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:47:28.312427
"""
def conta_multipli(a, b, c):
    n=0   
    for i in range(c+1):
        if (i%a)==0:
            if (i%b)!=0:
                n=n+1
    return n
    
a, b, c = map(int, input().split())
print(conta_multipli(a, b, c))
