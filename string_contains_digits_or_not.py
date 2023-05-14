t=int(input())
for i in range(t):
    n=input()
    s=0
    for i in n:
        if i=='1' or i=='3' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
            s='1'
            break
        else:
            pass
    if s=='1':
        print("Yes")
    else:
        print("No")