# introduction

from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print(" Quack! ")


class FlyBehavior(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print(" I fly! ")


class Duck(ABC):

    @abstractmethod
    def __init__(self):
        self.quack_behavior = QuackBehavior()
        self.fly_behavior = FlyBehavior()

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print(" I am a mallard duck! ")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()
