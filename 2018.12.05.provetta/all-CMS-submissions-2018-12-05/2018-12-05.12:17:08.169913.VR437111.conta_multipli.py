"""
* user:  VR437111
* fname: LUCA
* lname: CHIAVEGATO
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:17:08.169913
"""
def conta_multipli():
    a=int(input())
    b=int(input())
    c=int(input())
    i=0
    for z in range(1,c+1):
       
       if z%a==0 and z%b!=0:
          i=i+1
    print(i)             
conta_multipli()


