# Print Square Sequence using yield
#     Create Generator method such that every time it will returns a next square number

# for exmaple : 1 4 9 16 ..

def square_sequence_generator(limit):
    n=1
    count=0
    while count<limit:
        yield n**2
        n+=1
        count+=1


squares=square_sequence_generator(10)

for num in squares:
    print(num)