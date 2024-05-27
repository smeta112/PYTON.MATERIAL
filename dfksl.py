from main import Car

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal is speaking!")

class Cat(Animal):
    def speak(self):
        print("Cat is speaking!")

cat_1 = Cat("Name 1", 15)
print(cat_1.name)
cat_1.speak()

