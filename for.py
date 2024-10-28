# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

head_count=0
for heads in result:
    if heads=='heads':
        head_count+=1

print(f"Head appears {head_count} times")

# Print square of all numbers between 1 to 10 except even numbers

for i in range(1,11):
    if i%2!=0:
        print(i**2)

# Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

expense_enter=input('Enter expense amount')
expense_enter=int(expense_enter)

if expense_enter not in expense_list:
    print('No such expense found')

for i in range(len(expense_list)):
    if expense_enter==expense_list[i]:
        print(f'Expense in {month_list[i]} is {expense_enter}')

# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    ask=input('Are you tired')
    if i==5:
        print('congradulations')
    elif ask=='yes':
        break
    elif ask=='no':
        continue



# Write a program that prints following shape

# *
# **
# ***
# ****
# *****

str=''

for i in range(1,6):
    str=str+'*'
    print(str)