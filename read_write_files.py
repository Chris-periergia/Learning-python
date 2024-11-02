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

# stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,

# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
# Output.csv should look like this,

# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68


with open("D:\\Python\\stocks.csv",'r') as f,open("D:\\Python\\output.csv",'w') as output:
    next(f)
    output.write('Company Name,PE Ratio,PB Ratio\n')
    for line in f:
        line=line.strip('\n').split(',')

        Company,Price,Earnings_per_share, Book_Value=line[0],float(line[1]),float(line[2]),float(line[3])
        pe_ratio=format(Price/Earnings_per_share,'.2f')
        pb_ratio=format(Price/Book_Value,'.2f')

        output.write(f'{Company},{pe_ratio},{pb_ratio}\n')
        




