arr = ['hello', 'world',]
txt = ''
for i in arr:
    for j in range(len(i)):
        if j == 0:
            txt += str(ord(i[j]))
        else:
            txt += i[-j]
            print(j)
    txt += ' '
new = ''

# 65 119esi 111dl 111lw 108devi 105n 97n 111ka
# 65 119esi 111dl 111lw 108dvei 105n 97n 111ka

print(txt)