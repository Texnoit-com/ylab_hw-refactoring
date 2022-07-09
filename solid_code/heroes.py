'''1. Вынести оповещение в отдельный класс, занимающийся выводом информации.
   2. Создать классы-миксины для каждого оружия.
   3. Каждого супергероя реализовать как наследника SuperHero и вместо
      изменения базового класса переопределять нужные методы'''

from abc import abstractmethod
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
class SuperHero:
    name: str
    can_use_ultimate_attack: bool = True
    finder: AntagonistFinder = AntagonistFinder()

    @abstractmethod
    def attack(self):
        pass

    def find(self, place):
        self.finder.get_antagonist(place)


@dataclass(repr=False, eq=False)
class TaekwondoHero(SuperHero, Kick):

    def attack(self):
        self.roundhouse_kick()


@dataclass(repr=False, eq=False)
class ShootingHero(SuperHero, Gun):

    def attack(self):
        self.fire_a_gun()


@dataclass(repr=False, eq=False)
class EyeLasersHero(SuperHero, Laser):

    def attack(self):
        self.incinerate_with_lasers()

    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()


@dataclass(repr=False, eq=False)
class Superman(EyeLasersHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return 'Kick'
