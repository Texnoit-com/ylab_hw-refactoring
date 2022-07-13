'''1. Вынести оповещение в отдельный класс, занимающийся выводом информации.
   2. Создать классы-миксины для каждого оружия.
   3. Каждого супергероя реализовать как наследника SuperHero и вместо
      изменения базового класса переопределять нужные методы'''

from abc import ABC, abstractmethod
from dataclasses import dataclass

from antagonistfinder import AntagonistFinder


@dataclass(repr=False, eq=False)
class TV:
    name: str = 'Fox news'

    @staticmethod
    def create_news(place, name):
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')

    def planets(self, planet):
        planet_coordinates = getattr(planet, 'coordinates', 'place')
        print(f'{self.name} notifies {planet_coordinates}')


@dataclass(repr=False, eq=False)
class Punch():
    @staticmethod
    def punch():
        print('PUNCH!')


@dataclass(repr=False, eq=False)
class Gun():
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


@dataclass(repr=False, eq=False)
class Laser():
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


@dataclass(repr=False, eq=False)
class Kick():
    @staticmethod
    def roundhouse_kick():
        print('Bump')


@dataclass(repr=False, eq=False)
class SuperHero(ABC):
    name: str
    can_use_ultimate_attack: bool = True
    finder: AntagonistFinder = AntagonistFinder()

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass

    def find(self, place):
        self.finder.get_antagonist(place)


@dataclass(repr=False, eq=False)
class ChuckNorris(SuperHero, Gun, Kick):

    def __init__(self):
        super().__init__('Chuck Norris', False)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.fire_a_gun()


@dataclass(repr=False, eq=False)
class Superman(SuperHero, Laser, Punch):

    def __init__(self):
        super().__init__('Clark Kent', True)

    def attack(self):
        self.punch()

    def ultimate(self):
        self.incinerate_with_lasers()
