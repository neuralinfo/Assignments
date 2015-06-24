import json
import nltk
import os
from nltk.corpus import stopwords

input = open('index_file.txt')
lines = input.readlines()
f = None

os.system(u'aws s3 sync . s3://berkeley-w205-spooner-emr-output/assign2')

for line in lines:
    words = line.split()
    fname = words[0]
    count = int(words[1])
    print fname
    print count
    i = int(0)
    text_blob = open('text_blob.txt', 'w+')
    
    while True:
        print i
        f = open(fname+str(i)+'.json')        
        i = i + 1000
        json_block  = json.load(f)
        for each in json_block:
            line = each[u'text'].encode('utf-8').strip()
            text_blob.write(line)
        if i > count:
            break
    f_read = text_blob.read()
    #tokenizer = RegexpTokenizer(r'\w+')
    cleaned_words = []
    tokens = nltk.tokenize.word_tokenize(f_read)
    for word in tokens:
        if not word in stopwords.words('english'):
            cleaned_words.append(word)
    fdist1 = nltk.FreqDist(cleaned_words) 
    fdist1.plot(30, cumulative=True)
    text_blob.close()
    os.remove('text_blob.txt')
