# Single Inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(f"This is a {self.species}")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def show_breed(self):
        print(f"The breed is {self.breed}")


# Example usage of single inheritance
dog = Dog("Canine", "Poodle")
dog.show_species()
dog.show_breed()
