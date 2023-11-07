# Multilevel Inheritance
class Vehicle:
    def show_vehicle_info(self):
        print("This is a vehicle")


class Car(Vehicle):
    def show_car_info(self):
        print("This is a car")


class ElectricCar(Car):
    def show_electric_car_info(self):
        print("This is an electric car")


# Example usage of multilevel inheritance
electric_car = ElectricCar()
electric_car.show_vehicle_info()
electric_car.show_car_info()
electric_car.show_electric_car_info()
