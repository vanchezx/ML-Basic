from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle:
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        """Инициализация транспортного средства"""
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """Запуск двигателя"""
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError("Недостаточно топлива для запуска двигателя")
            self.started = True

    def move(self, distance: float):
        """Проверка доступной дистанции"""
        fuel_required = distance * self.fuel_consumption
        if self.fuel < fuel_required:
            raise NotEnoughFuel(f"Недостаточно топлива для преодоления дистанции\nНеобходимо :{fuel_required} Доступно: {self.fuel}")