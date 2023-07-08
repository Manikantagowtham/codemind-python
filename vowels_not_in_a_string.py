n=input()
v="aeiou"
k=[]
for i in v:
    if i not in n and i not in k:
        k.append(i)
if len(k)==0:
    print(0)
else:
    print(*k)