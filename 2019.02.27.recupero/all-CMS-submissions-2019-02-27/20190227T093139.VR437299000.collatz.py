"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 09:31:39.421799
"""

i=int(input("inserisci un numero"))
n = [i]
for i in (n):
   if i==1:  
      if i%2==0:
        i=i/2
           if i%3==0:
             i=3i+1
    n.append(i)

print(n)

