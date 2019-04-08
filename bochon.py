def unique(list1):
    list3 = []
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        if len(x)>0 :
            list3.append(x)

    return list3

def match(str,list3):
    for x in list3:
        if str[len(str)-len(x):]==x:
            str=str[:-len(x)]
            match(str,list3)
    return str



F4 = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bochon",'r', encoding="utf8")
bochon=F4.read()
bochon_spilit=bochon.split(" ")


F = open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\text_file\bochon_example",'r', encoding="utf8")
bochon_example1=F.read()
bochon_example=bochon_example1.split(" ")
x=0
while x<=(len(bochon_example)-1):
    if bochon_example[x]=="অজস্র":
        bochon_example[x]=bochon_example[x]+" "+bochon_example[x+1]
        bochon_example[x+1]=""
        x+=1
    elif bochon_example[x]=="অঢেল":
        bochon_example[x]=bochon_example[x]+" "+bochon_example[x+1]
        bochon_example[x+1]=""
        x+=1
    elif bochon_example[x]=="লাল" and bochon_example[x+1]=="লাল":
        bochon_example[x]=bochon_example[x]+" "+bochon_example[x+1]+" "+bochon_example[x+2]
        bochon_example[x+1]=""
        bochon_example[x + 2] = ""
        x+=1
        x+=1
    elif bochon_example[x]=="কাড়ি" and bochon_example[x+1]=="কাড়ি":
        bochon_example[x]=bochon_example[x]+" "+bochon_example[x+1]+" "+bochon_example[x+2]
        bochon_example[x+1]=""
        bochon_example[x + 2] = ""
        x+=1
        x+=1
    elif bochon_example[x]=="বড়" and bochon_example[x+1]=="বড়":
        bochon_example[x]=bochon_example[x]+" "+bochon_example[x+1]+" "+bochon_example[x+2]
        bochon_example[x+1]=""
        bochon_example[x + 2] = ""
        x+=1
        x+=1
    x+=1
bochon_example2=[]
for x in bochon_example:
    if len(x)>0:
        bochon_example2.append(x)
        #print(x)
x=0
while x<=(len(bochon_example2)-1):
    print(bochon_example2[x]," --> ",end="")
    str=bochon_example2[x]
    if str[:4]=="অজস্র":
        print(str[:4])
    elif str[:4]=="অঢেল":
        print(str[5:])
    elif str[:3]=="লাল" and str[4:7]=="লাল":
        print(str[4:7],"",str[8:])

    elif str[:4]=="কাড়ি" and str[5:9]=="কাড়ি":
        print(str[:4],"",str[10:])

    elif str[:2]=="বড়" and str[3:5]=="বড়":
        print(str[:2],"",str[6:])
    else:
        str = match(bochon_example2[x], bochon_spilit)
        print(str)
    x+=1
