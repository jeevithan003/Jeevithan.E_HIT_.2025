n=int(input())
if n%2==0:
    if n>=2 and n<=5:
        print("not weird")
    elif n>=6 and n<=20:
        print("weird")
    else:
        print("not weird")
else:
    print("weird")