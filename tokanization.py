F = open("data.txt", 'r', encoding="utf8")
str = F.read()

F2 = open("stopwords-bn.txt", 'r', encoding="utf8")
str2 = F2.read()
str3 = str2.split("\n")


for x in str3:
    str=(str.replace(" "+x+" "," "))


str2=""
str3=""
for x in str:
    str2+=(x.replace('‘', " "))
for x in str2:
    str3+=(x.replace('’', " "))
s=str3.split('।')


m2=[]
for x2 in s:
    s2 = x2.split('?')
    for x2 in s2:
        m2.append(x2)

m3=[]
for x2 in m2:
    s2 = x2.split('!')
    for x2 in s2:
        m3.append(x2)

m4 = []
for x2 in m3:
    s2 = x2.split(';')
    for x2 in s2:
        m4.append(x2)

m7=[]
for x in m4:
    if len(x)!= 0:
        m7.append(x)



for x in m7:
    print(x)
