"""
* user:  VR437128
* fname: SOFIA
* lname: SCHIO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:45:18.498660
"""
def conta_multipli(a,b,c):
    n=0
    i=1
    while i*a<=c :
        if(i*a%b!=0) :
            n=n+1
        i=i+1
    return n'''


def conta_multipli(a,b,c):
    n=c/a
    i=1
    while i*a*b<=c :
        n=n-1
        i=i+1
    return n
'''
