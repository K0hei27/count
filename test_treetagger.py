#import liblary
import treetaggerwrapper as ttw
import collections
import matplotlib.pyplot as plt
import csv

#read datas
with open('./input/1997.txt') as f:
    data = f.read()

#treetagging
tagger = ttw.TreeTagger(TAGLANG='en')
tags = tagger.TagText(data)

l = []
for tag in tags:
    tag = tag.split('\t')[2]
    l.append(tag)

l_in_not = [s for s in l if ',' not in s]
l_in_not = [s for s in l_in_not if '.' not in s]
l_in_not = [s for s in l_in_not if '(' not in s]
l_in_not = [s for s in l_in_not if ')' not in s]

#output
with open('./output/output.csv', 'w') as f:
    counter = collections.Counter(l_in_not)
    word_sum = counter.most_common()
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(word_sum[:50])

for a,b in word_sum[:50]:
    print(a, b)

#plot
x = [word_sum[:50][i][0] for i in range(0,50)]
y = [word_sum[:50][i][1] for i in range(0,50)]

plt.figure(figsize=(10,5))
plt.bar(x, y)
plt.xticks(rotation=90)
plt.title('Couting Words')
plt.xlabel('Word')
plt.ylabel('Number')
plt.show()
