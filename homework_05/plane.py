from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        cargo = self.cargo + amount
        if cargo > self.max_cargo:
            raise CargoOverload(f"Перегруз транспортного средства\nНевозможно загрузить {amount} кг, на борту {cargo} кг, максимально {self.max_cargo} кг.")
        self.cargo = cargo

    def remove_all_cargo(self):
        before_cargo = self.cargo
        self.cargo = 0
        return before_cargo