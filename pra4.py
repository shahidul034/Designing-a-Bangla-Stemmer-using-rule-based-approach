F = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\need\dataset", 'r', encoding="utf8")
dataset=F.read()

F1 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\need\bibokti1",'r', encoding="utf8")
bibokti1=F1.read()

F2 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\need\bibokti",'r', encoding="utf8")
bibokti2=F2.read()
F3 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\need\bochon",'r', encoding="utf8")
bochon=F3.read()

F4 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\need\extra_check_set",'r', encoding="utf8")
extra_check_set=F4.read()

mm=[]
def unique( list1):
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



def st1_match(str,list3):
    flag=False
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]

            flag=True
    return str,flag

def st2_match(str,list3):
    flag = False
    for x in list3:
        if str[len(str)-len(x):]==x:
            if x[0]=='*':
                str = str[:-len(x)+1]
            else:
                str = str[:-len(x)]
            flag=True

    return str,flag
def st3_match(str,list3):
    flag=False
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            flag=True
    return str,flag
def extra_check(str,list3):
    flag=False
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            flag=True
    return str,flag
def match(x):
    m=x.split(" ")
    for x2 in m:
        ss=x2
        str2,flag = st1_match(x2, bibokti121)
        str3, flag = st2_match(str2, bibokti211)
        str4, flag = st3_match(str3, bochon12)
        str5, flag = extra_check(str4, extra_check_set12)

        if len(str5)>=3:
            print(str5, end=" ")
            #pass
        elif len(str4)>=3:
            print(str4, end=" ")
            #pass
        elif len(str3)>=3:
            print(str3,end=" ")
            #pass
        else:
            print(ss, end=" ")
    print()



bibokti12=bibokti1.split(" ")
bibokti21=bibokti2.split(" ")
bochon1=bochon.split(" ")
extra_check_set1=extra_check_set.split(" ")
bibokti121=unique(bibokti12)
bibokti211=unique(bibokti21)
bochon12=unique(bochon1)
extra_check_set12=unique(extra_check_set1)

bibokti121.sort(key=len, reverse=True)
bibokti211.sort(key=len, reverse=True)
bochon12.sort(key=len, reverse=True)
extra_check_set12.sort(key=len, reverse=True)








dataset2=dataset.split('\n')

for x in dataset2:
    str=match(x)



