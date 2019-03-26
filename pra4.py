import math
def nxt_prime_num(n):
    x=2
    L={}
    for x in range(1,n+100):
        L[x]=0
    L[2]=0
    for x1 in range(2,n+100):
        for x in range(2,n+100):
            L[x*x1]=1
    for x in range(2,n+100):
        if L[x]==0 and x>n:
            print("prime: ",x)
            return x
def encrypt(msg,puk,n):
    msg1=pow(msg,puk)
    return msg1%n

def decrypt(msg,prk,n):
    msg1=pow(msg,prk)
    #print("de: ",msg1)
    return msg1%n


def rsa(p,q):
    n=p*q
    totient=(p-1)*(q-1)
    e=2
    while(e<totient):
        if math.gcd(e,totient)==1  :
            break
        else:
            e += 1
    print("public key: ",e)
    k=2
    d = (1 + (k * totient)) / e
    print("private key: ", int(d))
    aa=[]
    aa.append(float(e))
    aa.append(float(d))
    aa.append(float(n))
    return aa

msg=344
aa=rsa(nxt_prime_num(2),nxt_prime_num(6))
en=encrypt(msg,aa[0],aa[2])
print(en)

de=decrypt(en,aa[1],aa[2])
print(de)
