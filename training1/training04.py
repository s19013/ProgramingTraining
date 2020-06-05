import re
A = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

B = re.split(", |\. |\.| ",A)
B.pop()
C={}

for x, y in enumerate(B):
    # print(x,y)
    a = x + 1
    if a==1 or 5<=a<=9 or a==15 or a==16 or a==19:
        C[y[0]]=a
    else:
        C[y[0:2]]=a


print(C)