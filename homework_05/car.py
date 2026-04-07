from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float, engine: Engine = None):
        """Инициализация транспортного средства"""
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        """Установка двигателя на транспортное средство"""
        self.engine = engine