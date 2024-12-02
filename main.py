import random
from character import Hero, Goblin, Orc, Drangon
from battle import Battle


def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")
    hero = Hero(name, 100, 20, 5, speed=12, role=role)
    print(hero)

    monster_pool = [Goblin("고블린", 50, 10, 2, 1, 1),
                    Orc("오크", 50, 10, 2, 1, 1),
                    Drangon("드래곤", 50, 10, 2, 1, 1)]

    battle = Battle()
    while hero.is_alive():
        monster = random.choice(monster_pool)
        print(f"\n 몬스터 {monster.name} 등장!")
        print(monster.description())

        if not battle.fight(hero, monster):
            break


if __name__ == '__main__':
    main()

print("hello")
