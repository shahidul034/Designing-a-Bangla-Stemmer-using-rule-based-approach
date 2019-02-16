import os,codecs
import gensim, logging
from numpy import unicode
bd_corpus_path=r"D:\word to vector\Bengali-Word-Embedding\bd_corpus" # all files path [ folder name]
bd_save_model_path=r"D:\word to vector\Bengali-Word-Embedding\bd_save_model" # where i save model
test_path=bd_corpus_path+"/corpus_bd_01.txt" # data for testing
def read_file_for_test(path):
    sentences=[]
    with open(path,encoding="utf8") as r:
        for x in r.readlines():
            words=[y for y in x.split()]
            words=[get_unicode(y) for y in words]
            sentences.append(words)
    return sentences

def output_test(path):
    min_count = 1
    size = 100
    workers = 4
    window = 4
    lines = [get_unicode(x) for x in days.split()]
    model = gensim.models.Word2Vec(lines,
                                   min_count=min_count,
                                   size=size,
                                   workers=workers,
                                   window=window)

    print ("<>"*34)
    words=read_file_for_test(path)
    # print first 2 words embedding-vector
    for i in range(min(2,len(words))):
        print( "Words: ",words[i][0]," em-vec: ",model[words[i][0]])
        pass

    # print first 10 words embedding vectors similarity
    print ("*"*80)
    for i in range(min(10,len(words))):
        a=words[i][0]
        b=words[i+1][0]
        sim_vec=model.similarity(a,b)
        print( "words-sim-vec: ",sim_vec)



def chomps(s):
    return s.rstrip('\n')

def get_unicode(input):
    input=chomps(input)
    if type(input) != unicode:
        input =  input.decode('utf-8')
        return input
    else:
         return input

filename = r"C:\Users\Inception\PycharmProjects\FIRSTproject\corpus_bd_01.txt"
file = open(filename, encoding="utf8")
days = file.read()
#print(days)
min_count = 1
size = 100
workers = 4
window = 4
lines = [get_unicode(x) for x in days.split()]
model = gensim.models.Word2Vec(lines,
                               min_count=min_count,
                               size=size,
                               workers=workers,
                               window=window)

save_p = "D:" + '/model_corpus_bd'
model.save(save_p)

output_test(test_path)





'''
print(lines)

stop_words= ['এ']
cnt=0
unique_word=[]
for x in lines:
    for x1 in stop_words:
        if x==x1:
            cnt=1
            break
    if cnt==0:
        unique_word.append(x)
    cnt=0
print(unique_word)
'''