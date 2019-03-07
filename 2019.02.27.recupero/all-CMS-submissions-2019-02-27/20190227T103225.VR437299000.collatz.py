"""
* user:  VR437299000
* fname: ENRICO
* lname: MELEGATI
* task:  prova-collatz
* score: 0.0
* date:  2019-02-27 10:32:25.361553
"""
i=int(input())
print(i)
lista = [i]
while i>1:
      if i%2==0:
        i=i/2
      else:
          i=3*i+1
      print(i)
      lista.append(i)
#print(lista)

