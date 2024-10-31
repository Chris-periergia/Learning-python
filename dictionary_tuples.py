# We have following information on countries and their population (population is in crores),

# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population

countries_dict={'China':143,'India':136,'USA':32,'Pakistan':21}


# Write a program that asks user for three type of inputs,

print('Type print to print all countries with their population')
print('Type add to add a country to existing dictionary')
print('Type remove to remove a country from existing dictionary')

user_input=input('Enter print ,add ,remove (operations for country dictionary) ')

if user_input=='print':
    for country,population in countries_dict.items():
        print(f"{country}==>{population}")

# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

elif user_input=='add':
    country_name=input('Enter country name to add to dictionary')
    if country_name in countries_dict:
        print('This country already exists in dictionary')
    else:
         country_population=int(input('Enter population of that country'))
         countries_dict[country_name]=country_population
         print(f'The dictionary after adding {country_name} is {countries_dict}')

# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

elif user_input=='remove':
    country_name=input('Enter country name to remove from dictionary')
    if country_name in countries_dict:
        countries_dict.pop(country_name)
        print(f'Dictionary after removing {country_name} is')
        for country,population in countries_dict.items():
            print(f"{country}==>{population}")
    else:
         print('The dictionary after adding is ',countries_dict)

# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

print('Type country name to print its population')
user_input=input('Enter which country population you want to know')

if user_input in countries_dict:
    print(f'The population of {user_input} is {countries_dict[user_input]}')
else:
    print(f'The country does not exist in dictionary')



# You are given following list of stocks and their prices in last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]



# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stocks_dict={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}

stock_operation=input('Enter print,add')

def prinT(stocks):
    for key,value in stocks.items():
        print(f'{key}==>{value}==>avg:{format(sum(value)/len(value),'.2f')}')

def add(stocks):
    stock_ticker=input('Enter stock ticker')
    stock_price=int(input('Enter stock ticker price'))
    if stock_ticker in stocks:
         stocks[stock_ticker].append(stock_price)
    else:
        stocks.update({stock_ticker:[stock_price]})
    print(f'Dictionary updated : {stocks}')
    
if stock_operation=='print':
    prinT(stocks_dict)
elif stock_operation=='add':
    add(stocks_dict)


# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

radius=float(input('Enter radius of circle'))


def circle_calc(radius):
    area=3.14*(radius**2)
    circumference=2*3.13*radius
    diameter=2*radius
    circle_info=(area,circumference,diameter)
    return circle_info

area,circumference,diamter=circle_calc(radius)

print(f'Area={area} , Circumference={circumference} , Diameter={diamter}')