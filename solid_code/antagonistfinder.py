'''По SOLID: Создать абстрактный класс Place, обязывающий реализовать
метод для поиска злодея'''

from abc import ABC, abstractmethod
from dataclasses import dataclass

from places import Kostroma, Tokyo


@dataclass(repr=False, eq=False)
class Place(ABC):
    @abstractmethod
    def get_antagonist(self, place):
        pass


@dataclass(repr=False, eq=False)
class AntagonistFinder(Place):

    def get_antagonist(self, place):
        if isinstance(place, Kostroma):
            place.get_orcs()
        elif isinstance(place, Tokyo):
            place.get_godzilla()
