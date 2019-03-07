"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 10:12:19.358777
"""

i=int(input("inserisci un numero"))
print(i)
while i>1:
      if i%2==0:
        i=i/2
      else:
          i=3*i+1
      print(i)



