# You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length=92
width=48.8

area=length*width

print('The length of football field that is ',length,' meter long and ',width,' wide is ',format(area,'.2f'))

# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

packets_of_chips=9
packet_price=1.49

total_price=packets_of_chips*packet_price
money_given=20
money_left=money_given-total_price

print(money_left)

# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length_of_square=5.5

area_of_square=5.5**2

price_per_sq_feet=500

total_cost=area_of_square*price_per_sq_feet

print('total cost is ',total_cost)

# Print binary representation of number 17

number=13
binary=[]
print('Binary representation of ',number,' is ')
while number!=0:
    binary.append(str(number%2))
    number=int(number/2)

binary.reverse()

print("".join(binary))


