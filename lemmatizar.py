F = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\data_corpus", 'r', encoding="utf8")
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

def check_again(str,list3):
    if str[:-1]==dari:
        return str
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            check_again(str, list3)

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
        #str+=dari
        pass
    if last_char_roishi(str):
        str=str[:-1]
    return str


def match(str,list3):
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            match(str,list3)
    return str

unique(bibokti2)

for x in plain_text2:
    str=match(x,list3);
    print(str)





