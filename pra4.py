f=open(r"C:\Users\Inception\Desktop\1st.txt",'w',encoding="utf8")
f2=open(r"C:\Users\Inception\PycharmProjects\FIRSTproject\rafi_data",'r', encoding="utf8")
str=f2.read()
str2=str.split(",")
str3=""
for x in str2:
    str3+=(" "+x+" ")
str4=str3.split("\n")
str5=""
for x in str4:
    str5+=(" "+x+" ")

str6=str5.split()
#print(str6)
mm=""
for x in str6:
    mm+=x+" "
print(mm)
f.write(mm)