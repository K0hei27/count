#import liblary
import collections
import nltk
from nltk import stem
import glob
import matplotlib.pyplot as plt
import os
import csv

#read datas
files = sorted(glob.glob('./input/*.txt'))
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

# counting & output
with open('./output/outputs.csv', 'w') as f:
    for lem_list in lem_word_lists:
        counter = collections.Counter(lem_list)
        word_sum = counter.most_common()
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(word_sum[:50])
