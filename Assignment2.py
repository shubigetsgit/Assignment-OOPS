class Dog:
    def __init__(self,name, age, coat_color):
        self.name = name 
        self.age = age 
        self.coat_color = coat_color
    def description(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.name}")
    def get_info(self):
        print(f"Color : {self.coat_color}")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, weight ):
        super().__init__(name, age, coat_color)
        self.weight = weight
    def description(self):
        print(f"{self.name} is a JackRussellTerrier whose weight is {self.weight} pounds")
    def snoring(self):
        print(f"{self.name} is snoring while he is asleep")


class Bulldog(Dog): 
    def __init__(self, name, age, coat_color,pro ):
        super().__init__(name, age, coat_color)
        self.pro = pro
    def description(self):
        print(f"{self.name} is a Bulldog whose age is {self.age} years")
    def character(self):
        print(f"{self.name} is very {self.pro}")

dog1 = Dog("Rudolf", 5,  "White")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Perry", 6,  "Brown",50)
dog2.description()
dog2.snoring()

dog3 = Bulldog("Lola", 2,  "White&Brown","Cute")
dog3.description()
dog3.character()

