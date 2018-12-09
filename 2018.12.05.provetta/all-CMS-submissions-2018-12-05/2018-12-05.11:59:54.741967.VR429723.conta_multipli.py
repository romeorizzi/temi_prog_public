"""
* user:  VR429723
* fname: VERONICA
* lname: GUIDOLIN
* task:  conta_multipli
* score: 0.0
* date:  2018-12-05 11:59:54.741967
"""
a, b, c = map(int, input().split())
n=0
for i in range(1,c+1):
    if i%a==0:
        if i%b!=0:
            n=n+1
print(n)
