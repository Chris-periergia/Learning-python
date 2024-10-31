# poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

words_count={}

with open("D:\\Python\\poem.txt") as f:
    for line in f:
        each_line=line.split(' ')
        for word in each_line:
            if word in words_count:
                words_count[word]+=1
            else:
                words_count.update({word:1})

maximum_occured=list(words_count.values())

maximum_occured=max(maximum_occured)

print(f'The words that occured maximum times {maximum_occured} are')

for word,count in words_count.items():
    if count==maximum_occured:
        print(word)

