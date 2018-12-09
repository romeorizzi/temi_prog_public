"""
* user:  VR437257
* fname: BENEDETTA
* lname: TOMMASI
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 12:12:32.921603
"""
n1 = int(input())
n2 = int(input())

def play(n1, n2):
    if (n1==n2):
        return (0,0)
    if (n1>n2):
        return (n1-n2,0)
    if (n2>n1):
        return (0, n2-n1)   
    

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)
