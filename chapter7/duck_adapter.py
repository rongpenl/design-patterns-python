from abc import abstractmethod


class Duck():

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):

    def quack(self):
        print("I quack")

    def fly(self):
        print("I fly")


class Turkey():

    @abstractmethod
    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):

    def gobble(self):
        print("I gobble")

    def fly(self):
        print("I fly for a short distance")


class TurkeyAdapter(Duck):

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


if __name__ == "__main__":
    wild_turkey = WildTurkey()
    fake_duck = TurkeyAdapter(wild_turkey)
    fake_duck.fly()
    fake_duck.quack()
