# Decorator pattern
from abc import ABC, abstractclassmethod


class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self) -> str:
        return self.description

    @abstractclassmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    pass


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HomeBlend(Beverage):
    def __init__(self):
        self.description = "HomeBlend"

    def cost(self) -> float:
        return 0.89


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self._cost = 0.20

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + self._cost


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self._cost = 0.15

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + self._cost


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self._cost = 0.10

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + self._cost


if __name__ == "__main__":
    beverage = Espresso()
    beverage = Mocha(beverage)
    beverage = Soy(beverage)
    beverage = Whip(beverage)
    print(beverage.get_description(), beverage.cost())
    beverage = HomeBlend()
    beverage = Whip(beverage)
    print(beverage.get_description(), beverage.cost())
