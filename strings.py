# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

street='7A street'
city='lahore'
country='pakistan'

print('adress using + operator ')
address=street+'\n'+city+'\n'+country

print('adress using f-string method')
address=f"{street}'\n'{city}'\n'{country}"

# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

s='Earth revolves around the sun'

print('Print revolves using slice operator=',s[6:14])
print('Print sun using negative index=',s[-3:])


# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

fruits=4
vegetables=5

s=f"I eat {vegetables} veggies and {fruits} fruits daily"

print(s)

# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s='maina 200 banana khaye'
print('The original string is ',s)
s=s.replace('200','10').replace('banana','samosa')

print('String after replacing incorrect words is',s)
