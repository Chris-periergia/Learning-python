# Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Write a program that asks user to enter a city name and it should tell which country the city belongs to.

city=input('Enter a city name')

if city in india:
    print(f"{city} belongs to india")
elif city in pakistan:
    print(f"{city} belongs to pakistan")
elif city in bangladesh:
    print(f"{city} belongs to bangladesh")
else:
    print('None of lists contains entered city!!')

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country

city1=input('Enter city 1')
city2=input('Enter city 2')

if city1 in india and city2 in india:
    print('Both cities are in india') 
elif city1 in pakistan and city2 in pakistan:
    print('Both cities are in pakistan') 
elif city1 in bangladesh and city2 in bangladesh:
    print('Both cities are in bangladesh')
else:
    print('The cities are not in same country') 

# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

# Ask user to enter his fasting sugar level

sugar_level=input('Enter your sugar level')
sugar_level=int(sugar_level)

# If it is below 80 to 100 range then print that sugar is low

if sugar_level<80:
    print('Sugar is low')
# If it is above 100 then print that it is high otherwise print that it is normal
elif sugar_level>100:
    print('Sugar is high')
elif sugar_level>=80 and sugar_level<=100:
    print('Sugar is normal')