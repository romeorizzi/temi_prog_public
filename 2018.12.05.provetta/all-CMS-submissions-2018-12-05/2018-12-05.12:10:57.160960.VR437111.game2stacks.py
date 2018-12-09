"""
* user:  VR437111
* fname: LUCA
* lname: CHIAVEGATO
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:10:57.160960
"""
def play():
    n1=int(input())
    n2=int(input())
    Mn1=0
    Mn2=0
    if n1==n2:
       Mn1=0
       Mn2=0
    else:
        if n1<n2:
           Mn1=0
           Mn2=n2-n1
        else:
             Mn1=n1-n2
             Mn2=0
    print(Mn1)
    print(Mn2)
play()
       
