"""
* user:  VR437128
* fname: SOFIA
* lname: SCHIO
* task:  conta_inversioni
* score: 0.0
* date:  2018-12-05 12:44:19.675132
"""
def numero_di_inversioni(p):
    i=0
    n=0
    while i<len(p) :
        j=i
        while j<len(p) :
            if p[i]>p[j] :
                n=n+1
            j=j+1
        i=i+1
    return n
