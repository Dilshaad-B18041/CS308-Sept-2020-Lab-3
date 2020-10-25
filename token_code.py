def make_tokens(state):    
    import nltk
    import os,sys
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    #read the file from current directory
    token_file_name="token_count"
    file_name="browsed_file"
    
    if(state=="neglect"):
        file_name="exclude_file"
        token_file_name="token_count_"+file_name
    
    f=open(os.path.join(sys.path[0], file_name+'.txt'),'r')
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
    with open(os.path.join(sys.path[0], token_file_name+'.txt'),'w') as d:
        for i in token:
            st=i+" "+str(token[i])
            d.write(st)
            d.write("\n")
