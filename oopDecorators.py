from abc import ABC
from abc import abstractmethod

class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.b_n = brand_name
        self.y_of_i = year_of_issue
        self.b_p = base_price
        self.mg = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        return 0

    def vehicle_type(self) -> str:
        return self.b_n + " " + self.__class__.__name__

    def is_motorcycle(self) -> bool:
        if self.wheels_num() == 2:
            return True
        return False

    @property
    def purchase_price(self) -> float:
        price = self.b_p - 0.1 * self.mg
        if price < 100_000:
            price = 100_000
        return price

class Car(Vehicle):
    def wheels_num(self):
        return 4

class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2

class Truck(Vehicle):
    def wheels_num(self):
        return 10

class Bus(Vehicle):
    def wheels_num(self):
        return 6

vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
)

if __name__ == "__main__":
    for vehicle in vehicles:
        assert vehicle.vehicle_type() == "Toyota Car"
        assert vehicle.is_motorcycle() is False
        assert vehicle.purchase_price == 985000.0