from collections import Counter
a = 'This is a sentence that has multiple words. Each word from these words can appear multiple times. The purpose of this is to see the words that appear multiple times. And also the order of each word.'

c = Counter(a.lower().split(" "))

print(c)
