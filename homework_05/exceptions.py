class LowFuelError(Exception):
    """Недостаточно топлива для запуска двигателя"""
    pass

class NotEnoughFuel(Exception):
    """Недостаточно топлива для преодоления дистанции"""
    pass

class CargoOverload(Exception):
    """Перегруз транспортного средства"""
    pass
