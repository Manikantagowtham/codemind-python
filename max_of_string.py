s=input()
m=0
for i in s:
    if ord(i)>m:
        m=ord(i)
print(chr(m))