# Parent Class

class Animal:
    
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def eat(self, food):
        print(f"The {self.name} eats {food}.")
    
    def sleep(self):
        print(f"The {self.name} sleep peacefully.")

    def speak(self):
        print(f"The {self.name} makes a sound appropriate for a {self.species}.")

# Child Classes
class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, "Horse")
        self.speed = speed  # Speed in km/h
    
    def run(self):
        print(f"The {self.name} runs at a speed of {self.speed} km/h!")

class Duck(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age, "Duck")
        self.can_fly = can_fly  # Use boolean to indicate if the duck can fly
    
    def swim(self):
        print(f"The {self.name} swims in the pond.")
    
    def fly(self):
        if self.can_fly:
            print(f"The {self.name} flaps its wings and takes off!")
        else:
            print(f"The {self.name} cannot fly.")

class Sheep(Animal):
    def __init__(self, name, age, meat_yield):
        super().__init__(name, age, "Sheep")
        self.meat_yield = meat_yield  # meat produced in kilograms
    
    def graze(self):
        print(f"The {self.name} graze in the pasture.")
    
    def meat(self):
        print(f"The {self.name} produces {self.meat_yield} kg of meat!")

# Farm Class
class Farm:
    def __init__(self):
        self.animals = []  # List to store all animals on the farm
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the farm.")
    
    def list_animals(self):
        print("\nAnimals on the farm:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.species}, {animal.age} years old)")

# Main Function
def main():
    # Creating Farm
    my_farm = Farm()

    # Creating Animals
    FastX = Horse(name="FastX", age=7, speed=100)  # FastX is the best name for the horse whose speed is 100 :)
    KFS = Duck(name="KFS", age=2, can_fly=True)    # Just names
    Naive = Sheep(name="Naive", age=4, meat_yield=100)

    # Adding Animals to Farm
    my_farm.add_animal(FastX)
    my_farm.add_animal(KFS)
    my_farm.add_animal(Naive)

    # Listing Animals
    my_farm.list_animals()
    
    # Testing Animal Behaviors
    FastX.eat("hay")
    FastX.run()
    FastX.sleep()
    
    KFS.eat("grains")
    KFS.swim()
    KFS.fly()
    
    Naive.eat("grass")
    Naive.graze()
    Naive.meat()
    Naive.sleep()

if __name__ == "__main__":
    main()