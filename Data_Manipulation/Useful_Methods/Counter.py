# maps keys to counts in a dictionary, ei: a word count

from collections import Counter
c = Counter ([0, 1, 2, 0])      # c is (basically) {0: 2, 1: 1, 2: 1}

# a Counter has a most_common method that is frequently used
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)

