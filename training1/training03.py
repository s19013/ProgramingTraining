import re
A="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

B = re.split('[,\s\.]',A)
C=[]
for x in B:
    if len(x)==0:
        continue
    else:
        C.append(len(x))


print(C)

