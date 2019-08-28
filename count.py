#import liblary
import collections
import nltk
from nltk import stem
import matplotlib.pyplot as plt
import csv
#read datas
with open('./input/sample02.txt') as f:
    data = f.read()
    data = data.lower()

#lemmatize
wnl = stem.WordNetLemmatizer()
lem_word_list = []
for word in data.split():
    lem_word = wnl.lemmatize(word)
    lem_word_list.append(lem_word)

# counting & output
with open('./output/output.csv', 'w') as f:
    counter = collections.Counter(lem_word_list)
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
