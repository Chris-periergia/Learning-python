
# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")

class Human:
    def __init__(self,id,name):
        self.name=name
        self.id=id


emp1=Human(1,'coder')

print('before deleting anything : ',vars(emp1))

# Use del property to first delete id attribute and then the entire object

del emp1.id

print('After deleting id : ',vars(emp1))

try:
    del emp1
    print('Employee has been deleted')
except Exception as e:
    print(e.__class__.__name__,emp1)