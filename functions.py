# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

base=input('Enter base')
base=float(base)
height=input('Enter height')
height=float(height)
shape=input('Enter shape')

def calculate_area(base,height,shape='triangle'):
    area=0
    if shape=='triangle':
        area=(1/2)*base*height
    elif shape=='rectangle':
        area=base*height
    return area

print(calculate_area(base,height))


# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)


num=input('Enter number')
num=int(num)

def print_pattern(num):
    
    for i in range(1,num+1):
        print('*'*i)

print_pattern(num)