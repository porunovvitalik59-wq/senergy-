class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

autobus_1 = Transport("Renaul Logan", 180, 12)

print(f"Название автомобиля: {autobus_1.name} Скорость: {autobus_1.max_speed} Пробег: {autobus_1.mileage}")


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


autobus_2 = Autobus("Renaul Logan", 180, 12)

print(autobus_2.seating_capacity())
