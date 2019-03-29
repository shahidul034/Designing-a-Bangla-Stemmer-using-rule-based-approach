########### File read
F = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\data_corpus", 'r', encoding="utf8")
plain_text = F.read()
F2 = open(r"bibokti",'r', encoding="utf8")
bibokti=F2.read()
F3 = open(r"2nd_step_file",'r', encoding="utf8")
bibokti2_1=F3.read()


#############File spilit
bibokti2=bibokti.split(" ")
bibokti3=bibokti2_1.split(" ")
plain_text2=plain_text.split(" ")


############## Extra variable declaration
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
    list3 = []
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        if len(x)>0 :
            if x[0]=="*":
                list3.append(x[1:])
                mm.append(x[1:])
            else:
                list3.append(x)
    return list3


def sec_match(str,list3):
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            match(str,list3)
    return str

def match(str,list3):
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            match(str,list3)
    return str

##############Main function

list4=unique(bibokti2)
list5=unique(bibokti3)


for x in plain_text2:
    str=match(x,list4)
    str=sec_match(str,list5)
    str = sec_match(str, list5)
    print(str)





