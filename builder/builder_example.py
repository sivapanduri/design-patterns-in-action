class Car:
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
    def show(self):
        print("Car built with:", ", ".join(self.parts))

class CarBuilder:
    def __init__(self):
        self.car = Car()
    def add_wheels(self): self.car.add("Wheels"); return self
    def add_engine(self): self.car.add("Engine"); return self
    def build(self): return self.car

if __name__ == "__main__":
    builder = CarBuilder()
    car = builder.add_wheels().add_engine().build()
    car.show()
