def func():
    x=int(input())
    y=int(input())
    z=int(input())

    a=int(input())
    b=int(input())
    c=int(input())

    if x >a :
        ans='NO'
        return ans

    else:
        a-=x
        ans='YES'

    if y > (a+b):
        ans='NO'
        return ans
    else:
        if a>=y:
            a-=y
        else:
            b+=a
            b-=y
            a=0
    if z> (a+b+c):
        ans='NO'
    else:
        ans='YES'
    return ans

print(func())