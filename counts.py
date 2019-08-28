#import liblary
import collections
import nltk
from nltk import stem
import glob
import matplotlib.pyplot as plt

#read datas
files = sorted(glob.glob('./data/*.txt'))
data_list = []
for file in files:
    with open(file) as f:
        data = f.read()
        data = data.lower()
        data_list.append(data)

#lemmatize
lem_word_lists = []
for data in data_list:
    wnl = stem.WordNetLemmatizer()
    lem_word_list = []
    for word in data.split():
        lem_word = wnl.lemmatize(word)
        lem_word_list.append(lem_word)
    lem_word_lists.append(lem_word_list)

# counting : 要素と出現回数の組み合わせのオブジェクトを返す
for lem_list in lem_word_lists:
    counter = collections.Counter(lem_list)
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
