import json
import nltk
import os
import csv
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

    #clean words    
    cleaned_words = []
    tokens = nltk.tokenize.word_tokenize(f_read)
    for word in tokens:
        if not word in stopwords.words('english'):
            cleaned_words.append(word)

    #normalize
    cleaned_words = [w.lower() for w in cleaned_words]
        
    #gets counts
    freq={}
    for word in cleaned_words:
        if freq.has_key(word):
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    #wrtie out csv hist                
    csv_hist = open("hist_"+fname+".csv", "w")
    hist_write = csv.writer(csv_hist)
    hist_write.writerow(["word", "freq"])
    for word in sorted(freq.keys()):
        hist_write.writerow([word,freq[word]])
    csv_hist.close()

    #create hist plots    
    fdist1 = nltk.FreqDist(cleaned_words) 
    fdist1.plot(30, cumulative=True)
    text_blob.close()
    os.remove('text_blob.txt')
