"""
For the installation of wordcloud package:



I was struggling to find a way to do this within the PyCharm UI, but it is possible through the integrated Python console:

    Load your project with the appropriate VE
    Under the Tools dropdown, click Python Console

    Then use pip from within the console:

    import pip
    pip.main(['install','packagename'])


"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

with open('HarryPotter.txt', encoding='UTF-8') as f:
    text = f.readlines()

# Build the list of the words in the file. Do not change the punctuation.
single_words = []

for row in text:
    for elem in row.split():
        single_words.append(elem)


# Remove all punctuation at the beginning or end of each word.
# The result must be a new list of words.
clean_list = []

for elem in single_words:
    if elem == '—':
        del elem
    else:
        clean_list.append(elem.lower().strip(r".,?!@#€:);!(’"))


count_dict = {}

for elem in clean_list:
    if elem not in count_dict:
        count_dict[elem] = 1
    count_dict[elem] += 1

# Create a list of words that you don't want and then iterate
# through with the next for to eliminate them
unwanted_words = ['if',
                  'you',
                  'and',
                  'a',
                  'of',
                  'the',
                  'by',
                  'is',
                  'it',
                  'most',
                  'are',
                  'with',
                  'to',
                  'for',
                  'in',
                  'on',
                  'this',
                  'that',
                 '\\n']
# Delete words like 'And', 'Or', etc... from the dictionary
# It works only if you make a copy;
for key in count_dict.copy():
    if key in unwanted_words:
        count_dict.pop(key)

# print(count_dict)


# Creating empty WordCloud object and generating actual WordCloud.
wordcloud = WordCloud(max_words=10).generate_from_frequencies(count_dict)


# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
