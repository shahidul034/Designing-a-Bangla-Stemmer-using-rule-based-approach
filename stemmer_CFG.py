F1 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bibokti1",'r', encoding="utf8")
bibokti1=F1.read()

F2 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bibokti",'r', encoding="utf8")
bibokti2=F2.read()
F3 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bochon",'r', encoding="utf8")
bochon=F3.read()


def unique( list1):
    list3 = []
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        if len(x)>0 :
            if x[0]=="*":
                list3.append(x[1:])
            else:
                list3.append(x)
    return list3
def str_re(st):
    re_str = " --> ε"
    ss=st+re_str
    print(ss)

stem_cfg=bibokti1.split(" ")
stem_cfg12=unique(stem_cfg)

stem_cfg2=bibokti2.split(" ")
stem_cfg21=unique(stem_cfg2)

stem_cfg3=bochon.split(" ")
stem_cfg31=unique(stem_cfg3)


for x in stem_cfg12:
    str_re(x)
for x in stem_cfg21:
    str_re(x)
for x in stem_cfg31:
    str_re(x)