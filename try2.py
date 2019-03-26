F = open("corpus_bd_01.txt", 'r', encoding="utf8")
plain_text = F.read()
F2 = open(r"bibokti",'r', encoding="utf8")
bibokti=F2.read()
bibokti2=bibokti.split(" ")
plain_text2=plain_text.split(" ")


list3=[]
map={}
mm=[]
dari='া'

for x in plain_text2:
    map[x]=0


def place_dari(str):
    for x in mm:
        if str==x:
            return False
    return True
def unique(list1):
    list_set = set(list1)

    unique_list = (list(list_set))
    for x in unique_list:
        if len(x)>0 :
            if x[0]=="*":
                list3.append(x[1:])
                mm.append(x[1:])
            else:
                list3.append(x)

def replace(x,x2):
    x2 = -x2
    str = x[:x2]
    if place_dari(str):
        str+=dari

    return str


def match(x,x2):
    v = len(x) - 1
    v2 = len(x2) - 1
    cnt = v2 + 1
    cnt2 = 0
    while (v2 >= 0 and v>=0):
        if x[v] == x2[v2]:
            cnt2 += 1
        v2 -= 1
        v -= 1
    if cnt == cnt2:
        return True
    else:
        return False

unique(bibokti2)


for x in plain_text2:
    for x2 in list3:
        if match(x,x2) and map[x]==0:
            map[x]=1
            str=replace(x,len(x2))
            print(str)





