import random

A="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# print(word_list)


def fname(arg):
    word_list = arg.split()
    rw=""
    for w in word_list:
        if len(w)>4:
            s=w[0]
            e=w[-1]
            i=w[1:-1]
            box=list(i)
            random.shuffle(box)
            rw+=s+"".join(box)+e+" "
        else:
            rw+=w+" "
    return rw

print(fname(A))
