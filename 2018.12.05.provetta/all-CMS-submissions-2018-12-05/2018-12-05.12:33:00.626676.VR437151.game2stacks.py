"""
* user:  VR437151
* fname: GIACOMO
* lname: BARTOLI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:33:00.626676
"""
n1 = int(input())
n2 = int(input())

def play(n1, n2):  
    if n1 < n2:
        d = n2 - n1
        return (0,d)
    else:
        d = n1- n2
        return (d,0)
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)

