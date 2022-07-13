from typing import Union

from heroes import TV, ChuckNorris, SuperHero, Superman
from places import Earth, Kostroma, Mars, Tokyo

PLACE: set = (Kostroma, Tokyo, Earth, Mars)


def save_the_place(hero: SuperHero, place: Union[PLACE]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    TV().create_news(place, hero.name)
    TV().planets(Earth)
    TV().planets(Mars)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())
