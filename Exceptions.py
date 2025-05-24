# Create a custom exception AdultException.

# Create a class Person with attributes name and age in it.

# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.

# Create a function display_person() which prints the age and name of a person.

# let us say,

# if age>18 
#     he is major
# else
#     raise exception

# create cusomException named ismajor and raise it if age<18.

class AdultException(Exception):
    def __init__(self, msg):
        self.msg=msg
    def handle(self):
        print('AdultException Occured : ',self.msg)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_minor_age(self):
        try:

            if self.age>18:
                raise AdultException('The person is adult.')
            else:
                return self.age
        except AdultException as e:
            e.handle()
           
    
    def display_person(self):
        print(f'Name : {self.name}  ,  Age : {self.age}')


# Testing
person1=Person('Alice',17)
person1.display_person()
person1.get_minor_age()