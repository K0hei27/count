#import liblary
import collections
import nltk
from nltk import stem
import matplotlib.pyplot as plt

#read datas
with open('./data/sample02.txt') as f:
    data = f.read()
    data = data.lower()

#lemmatize
wnl = stem.WordNetLemmatizer()
lem_word_list = []
for word in data.split():
    lem_word = wnl.lemmatize(word)
    lem_word_list.append(lem_word)

# counting : 要素と出現回数の組み合わせのオブジェクトを返す
counter = collections.Counter(lem_word_list)
word_num = counter.most_common()
print(word_num)

#plot
x = [word_num[:50][i][0] for i in range(0,50)]
y = [word_num[:50][i][1] for i in range(0,50)]

plt.figure(figsize=(10,5))
plt.bar(x, y)
plt.xticks(rotation=90)
plt.title('Couting Words')
plt.xlabel('Word')
plt.ylabel('Number')
plt.show()
