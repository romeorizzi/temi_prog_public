"""
* user:  VR429674
* fname: CHIARA
* lname: MAFFEIS
* task:  conta_multipli
* score: 100.0
* date:  2018-12-05 12:15:01.334582
"""
def conta_multipli(a, b, c):
    conta=0
    for i in range(a,c+1):
        if i%a==0:
            if i%b!=0:
                conta+=1    
                       
    return conta 
    
a, b, c = map(int,raw_input().split())
print(conta_multipli(a, b, c))



















#a, b, c = map(int, input().split())
#print(conta_multipli(a, b, c))
