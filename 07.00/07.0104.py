# Hybrid Inheritance
class A:
    def show_A(self):
        print("This is from class A")


class B(A):
    def show_B(self):
        print("This is from class B")


class C(A):
    def show_C(self):
        print("This is from class C")


class D(B, C):
    def show_D(self):
        print("This is from class D")


# Example usage of hybrid inheritance
d = D()
d.show_A()
d.show_B()
d.show_C()
d.show_D()
