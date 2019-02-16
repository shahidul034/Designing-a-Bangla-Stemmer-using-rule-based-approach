F = open("data.txt", 'r', encoding="utf8")
str = F.read()
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

m5=[]
for x in m4:
    x2=x.replace('’',"")
    m5.append(x2)
m6=[]
for x in m5:
    x2=x.replace('‘',"")
    m6.append(x2)
for x in m6:
    if len(x)!=0:
        print(x)



