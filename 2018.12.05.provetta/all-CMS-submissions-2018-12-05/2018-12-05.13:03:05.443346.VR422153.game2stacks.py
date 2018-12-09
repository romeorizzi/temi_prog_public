"""
* user:  VR422153
* fname: ELEONORA
* lname: GIACOMELLI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:03:05.443346
"""
n1 = int(input())
n2 = int(input())

def play(n1, n2):  # questa è la funzione che devi perfezionare
    togli1=0
    togli2=0
    if (n1>n2):
        togli1=n1-n2
    if (n2>n1):
        togli2=n2-n1
    return(togli1,togli2)


    #return (0,0)   # non arrenderti sempre!
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

