graph = {'Oradea': ['Zerind', 'Sibiu'], 'Zerind': ['Oradea', 'Arad'], 'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
         'Timisoara': ['Arad', 'Lugoj'], 'Lugoj': ['Timisoara', 'Mehadia'], 'Mehadia': ['Lugoj', 'Dobreta'],
         'Dobreta': ['Mehadia', 'Craiova'], 'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
         'Sibiu': ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'], 'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
         'Fagaras': ['Sibiu', 'Bucharest'], 'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Craiova'],
         'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'], 'Giurgiu': ['Bucharest'],
         'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'], 'Hirsova': ['Urziceni', 'Eforie'], 'Eforie': ['Hirsova'],
         'Vaslui': ['Urziceni', 'Iasi'], 'Iasi': ['Vaslui', 'Neamt'], 'Neamt': ['Iasi']}
f=open("file2.txt","w")
str=""
tup={}
'''
for x in graph.items():
    #str+=(x[0]+" ")
    #print(x[0]," ",end="")
    for x1 in x[1]:
        print(x[0]," ",x1)
        str+=(x[0]+" "+x1+"\n")
f.write(str)
'''
f2=open(r"C:\Users\Inception\Desktop\new 3.txt","r")
str=f2.read()
str2=str.split('\n')
m=[]
for x in str2:
    s=x.split(" ")
    ss=""
    #print(s[1])

    '''
    
    m=0
    for mm in s:
        print(s[m])
        m+=1
    '''

    
    
    
    if s.__contains__("Rimnicu"):
        if s[0]=="Rimnicu":
            ss += (s[0] + " " + s[1])
            print(ss+","+s[2]+","+s[3])
            #tup[ss][s[2]]=int(s[3])
        else:
            ss += (s[1] + " " + s[2])
            print(s[0] + "," + ss +"," +s[3])
            #tup[s[0]][ss] = int(s[3])

    else:
        print(s)
        tup[s[0]][s[1]] = int(s[2])
