#Code Exercise
class Vehicle:
    """
    name: str
    max_speed: int
    capacity: int
    """
    def __init__(self):
        self.name = "Corki"
        self.max_speed = 50
        self.capacity = 5
    def  vroom(self) -> None:
        print("Vroom" * self.max_speed)

class Bus(Vehicle):
    def fare(self, age: int) -> None:
        """Tells how much fare is for a particular age"""
        if age >= 0 and age <= 17:
            print("Your ride is free!")
        elif age <= 60:
            print("The fare of this bus ride is $5.00.")
        else:
            print("Your ride is free!")

a_bus = Vehicle()
a_bus.vroom()

a_bus = Bus()
a_bus.name = "Tranlink Bus - 407"
a_bus.capacity = 35
a_bus.max_speed = 140
a_bus.fare(10)
a_bus.fare(35)
a_bus.fare(22)
a_bus.fare(78)