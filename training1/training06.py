import re
A="paraparaparadise"
B="paragraph"
X=[]
Y=[]
wa=[]
seki=[]
sa=[]

def letter_bigram(C):
    list=[]
    for i in range(len(C)):
        out = C[i:i+2]
        if  len(out) !=1:
            list.append(out)
    return list

X=letter_bigram(A)
Y=letter_bigram(B)
X=set(X)
Y=set(Y)
wa= X | Y
seki=X&Y
sa=X-Y


print(X,Y)
print(wa)
print(seki)
print(sa)
print("se" in wa)