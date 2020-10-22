def make_tokens():    
    import nltk
    import os,sys
    #read the file from current directory
    f=open(os.path.join(sys.path[0], 'browsed_file.txt'),'r')
    f=f.read()
    word=nltk.word_tokenize(f)
    tagged = nltk.pos_tag(word)
    token={}
    for j in tagged:
        if(len(j[0])>1 and j[1]!='IN' and j[1]!='DT'):
            try:
                token[j[0]]+=1
            except KeyError:
                token[j[0]]=1
    with open(os.path.join(sys.path[0], 'token_count.txt'),'w') as d:
        for i in token:
            st=i+" "+str(token[i])
            d.write(st)
            d.write("\n")
make_tokens()

