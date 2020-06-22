def cipher(A):
    result = ""
    for a in A:
        if a.islower():
            result += chr(219 - ord(a))
        else:
            result +=a
    return result

mojiretu=input("入力:")
anngou = cipher(mojiretu)
print("暗号化:" + anngou)

fukugen = cipher(anngou)
print("復元:" + fukugen)

if mojiretu==fukugen:
    print("成功")
else:
    print("失敗")