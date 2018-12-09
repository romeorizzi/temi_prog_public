"""
* user:  VR429723
* fname: VERONICA
* lname: GUIDOLIN
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 12:01:11.775393
"""
a=int(input())
b=int(input())
c=int(input())
n=0
for i in range(1,c+1):
    if i%a==0:
        if i%b!=0:
            n=n+1
print(n)
