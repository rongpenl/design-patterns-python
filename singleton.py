# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton():
    _instance = None

    def __init__(self):
        if Singleton._instance is None:
            Singleton._instance = self

    @staticmethod
    def get_singleton():
        return Singleton._instance


print(id(Singleton()))
singleton1 = Singleton().get_singleton()
print(id(singleton1))
singleton2 = Singleton().get_singleton()
print(id(singleton2))
