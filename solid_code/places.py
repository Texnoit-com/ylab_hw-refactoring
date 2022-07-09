from abc import ABC
from dataclasses import dataclass
from typing import ClassVar, List


@dataclass(repr=False, eq=False)
class Kostroma:
    city_name: ClassVar = 'Kostroma'

    def get_orcs(self):
        print('Orcs hid in the forest')


@dataclass(repr=False, eq=False)
class Tokyo:
    name: ClassVar = 'Tokyo'

    def get_godzilla(self):
        print('Godzilla stands near a skyscraper')


@dataclass(repr=False, eq=False)
class Planet(ABC):
    coordinates: List[float]


@dataclass(repr=False, eq=False)
class Earth(Planet):
    coordinates = [1, 1]


@dataclass(repr=False, eq=False)
class Mars(Planet):
    coordinates = [2, 2]
