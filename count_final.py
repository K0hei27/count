#import liblary
import collections
import csv
import glob
import matplotlib.pyplot as plt
import treetaggerwrapper as ttw



#read & joint
DATA_PATH = "./input/"
files = sorted(glob.glob('{}*.txt'.format(DATA_PATH)))

concat = ''
for file in files:
    concat += open(file,"r").read()
#delete words
concat = concat.replace('\n','')
concat = concat.replace('(A)','')
concat = concat.replace('(B)','')
concat = concat.replace(',','')
concat = concat.replace('.','')

#treetagging
tagger = ttw.TreeTagger(TAGLANG='en',TAGDIR='./')
tags = tagger.TagText(concat)

l = []
for tag in tags:
    tag = tag.split('\t')[2]
    l.append(tag)

# counting & output
with open('./output/output.csv', 'w') as f:
    counter = collections.Counter(l)
    word_sum = counter.most_common()
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(word_sum)

#plot & output
x = [word_sum[i][0] for i in range(0,len(word_sum))]
y = [word_sum[i][1] for i in range(0,len(word_sum))]
plt.figure(figsize=(10,5))
plt.bar(x, y)
plt.xticks(rotation=90)
plt.title('Couting Words')
plt.xlabel('Word')
plt.ylabel('Number')
plt.savefig('./output/word_count')
