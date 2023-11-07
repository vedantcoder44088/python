# Base class
class Parent:
    def show(self):
        print("Parent's show method")


# Derived class overriding the show method
class Child(Parent):
    def show(self):
        print("Child's show method")


# Instantiating the classes
parent = Parent()
child = Child()

# Calling the overridden methods
parent.show()  # Output: Parent's show method
child.show()   # Output: Child's show method
