"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 09:59:27.947240
"""

i=int(input("inserisci un numero"))
while i>1:
      if i%2==0:
        i=i/2
        print(i)
      else:
          i=3*i+1
    

print(i)

