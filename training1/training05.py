A="I am an NLPer"
def words_bigram():
    return A.split(" ")

def letter_bigram():
    list=[]
    for i in range(len(A)):
        B = A[i:i+1]
        if  B !=" ":
            list.append(B)
    return list

print(words_bigram())
print(letter_bigram())