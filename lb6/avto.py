from abc import ABCMeta, abstractmethod, abstractproperty, ABC


class Avto:
    __metaclass__ = ABCMeta

    def __init__(self, avto_type: str, avto_cost: str, avto_speed: int, avto_year: int):
        self.avto_type = avto_type
        self.cost = avto_cost
        self.speed = avto_speed
        self.year = avto_year

    @property
    @abstractmethod
    def height(self, x: int, y: int, z: int):
        print(self.avto_type)
        print(x, y, z)

    @property
    @abstractmethod
    def passengers_count(self, count: int):
        print(self.avto_type)
        print(count)

    @property
    @abstractmethod
    def home_port(self, port: str):
        print(self.avto_type)
        print(port)


class Aircraft(Avto, ABC):

    def height(self, x, y, z):
        print(self.avto_type)
        print(x, y, z)

    def passengers_count(self, count):
        print(self.avto_type)
        print(count)


class Ship(Avto, ABC):
    def passengers_count(self, count):
        print(self.avto_type)
        print(count)

    def home_port(self, port):
        print(self.avto_type)
        print(port)


ship = Ship("300", "Vessel", 90, 2013)
ship.home_port("Singapour")