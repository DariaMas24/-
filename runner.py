class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Имя бегуна должно быть строкой.")
        if speed <= 0:
            raise ValueError("Скорость бегуна должна быть положительной.")

        self.name = name
        self.speed = speed

    def run(self):
        print(f"{self.name} бежит со скоростью {self.speed}.")