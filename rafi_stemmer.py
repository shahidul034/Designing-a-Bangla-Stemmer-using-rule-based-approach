F = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bangla_stemmer_rafi", 'r', encoding="utf8")
F2 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\rafi_data_original.txt", 'r', encoding="utf8")
stemmer_data=F.read()
data=F2.read()

stemmer_data2=stemmer_data.split(" ")
data2=data.split(" ")

def match(str,list3):
    for x in list3:
        if str[len(str)-len(x):]==x :
            str=str[:-len(x)]
            match(str,list3)
            break
    return str
def again_check(str):
    if str[-3:]=="েরট":
        return str[:-3]
    elif str[-2:0]=="ের":
        return str[-2:0]

    return str

for x in data2:
    print(x,"--> ",end="")
    str=match(x,stemmer_data2);
    str=again_check(str)
    print(str)



