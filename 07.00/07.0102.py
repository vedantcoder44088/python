# Multiple Inheritance
class A:
    def show_A(self):
        print("This is from class A")


class B:
    def show_B(self):
        print("This is from class B")


class C(A, B):
    def show_C(self):
        print("This is from class C")


# Example usage of multiple inheritance
c = C()
c.show_A()
c.show_B()
c.show_C()
