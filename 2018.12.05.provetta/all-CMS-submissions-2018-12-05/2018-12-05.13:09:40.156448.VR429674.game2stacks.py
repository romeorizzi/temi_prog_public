"""
* user:  VR429674
* fname: CHIARA
* lname: MAFFEIS
* task:  game2stacks
* score: 100.0
* date:  2018-12-05 13:09:40.156448
"""
n1 = int(input())
n2 = int(input())

def play(n1, n2):  
    if (n1!=n2):
        if (n1>n2):
            return(n1-n2,0)
        else:
            return(0,n2-n1)
    else:
        return(0,0)  

togli1, togli2 = play(n1, n2)
print(togli1)
print(togli2)
