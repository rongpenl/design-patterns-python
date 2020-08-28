from abc import ABC, abstractclassmethod


class Observer(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class Display(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def display(self):
        pass


class Subject(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractclassmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractclassmethod
    def notify_observer(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self._observers = set()
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer: Observer):
        self._observers.add(observer)

    def remove_observer(self, observer, Observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
            # print("Weather Data is updating {}".format(str(observer)))

    def measure_changed(self):
        self.notify_observer()

    def set_measurement(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measure_changed()


class CurrentConditionDisplay(Observer, Display):
    def __init__(self, weather_data: WeatherData):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._temperature = None
        self._humidity = None

    def __repr__(self):
        return "a condition display"

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temp = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print("humidity:{},pressure:{},temperature:{}".format(self._humidity,
                                                              self._pressure,
                                                              self._temp))


class StatisticsDisplay(Observer, Display):
    def __init__(self, weather_data: WeatherData):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._temperatures = []
        self._stats = {"min": None, "max": None, "ave": None}

    def __repr__(self):
        return "a statistics display"

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperatures.append(temperature)
        self._stats["min"] = min(self._temperatures)
        self._stats["max"] = max(self._temperatures)
        self._stats["ave"] = sum(self._temperatures)/(len(self._temperatures))
        self.display()

    def display(self):
        print("Avg/Max/Min temperature = {}/{}/{}".format(self._stats["ave"],
                                                          self._stats["max"],
                                                          self._stats["min"]))


class PredictionDisplay(Observer, Display):
    def __init__(self, weather_data: WeatherData):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def __repr__(self):
        return "a prediction display"

    def update(self, temperature: float, humidity: float, pressure: float):
        self.display()

    def display(self):
        print("Building Predictions")


class WeatherStation():
    def __init__(self):
        weather_data = WeatherData()
        CurrentConditionDisplay(weather_data)
        StatisticsDisplay(weather_data)
        PredictionDisplay(weather_data)
        weather_data.set_measurement(1, 101, 10001)
        weather_data.set_measurement(2, 102, 10002)
        weather_data.set_measurement(3, 103, 10003)


if __name__ == "__main__":
    WeatherStation()
