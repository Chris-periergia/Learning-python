# create inheritance using animal Dog relation.
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 

# use super() constructor for calling parent constructor.
# class Animal:
#     #code

# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.

class Animal:
    def __init__(self,habitat):
        print('I am in animal constructor')
        self.habitat=habitat

    def Habitat(self):
        print(self.habitat)


class Dog(Animal):

    def __init__(self):
       super().__init__("prairies, deserts, grasslands, forests, rain forests, coastal regions and arctic zones")
    
    def Sound(self):
        print('Barks')

d=Dog()
d.Habitat()
d.Sound()
