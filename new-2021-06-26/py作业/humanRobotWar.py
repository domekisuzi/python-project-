"""made by @domekisuzi
    3/18
"""

"""
    游戏说明:游戏由三个hero和boss进行对抗,游戏采取多线程的方式进行(只运用了基础知识,处理的并非很好),boss会根据随机数,
    在一个回合里随机对三个hero进行攻击(即可能进攻0,3个hero),hero每个回合攻击一次,每个单位(boss或者hero)攻击完后,会
    休息一段时间,boss会根据所攻击的hero是否存活,来进行攻击或者回血,任何单位死亡都会停止自身的攻击
"""

import threading
import time
import random


class Boss:
    def __init__(self, name, hp, attack):
        self.__name = name
        self.hp = hp
        self.__attack = attack

    def attack(self, hero):
        if isinstance(hero, Hero):
            if hero.hp <= 0:
                self.hp += self.__attack
                print("boss回复了" + str(self.__attack) + "点血量")
            else:
                hero.hp -= self.__attack
                print("boss" + self.__name + "对勇士" + hero.name + "造成了" + str(self.__attack) + "点伤害")
                if hero.hp <= 0:
                    hero.alive = False
                    print("勇士" + hero.name + "倒下了")
        else:
            print("类型错误")
            return


class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.alive = True
        self.__attck = attack

    def attack(self, boss):
        if self.alive == True:
            if isinstance(boss, Boss):
                boss.hp -= self.__attck
                print("勇士" + self.name + "对boss造成了" + str(self.__attck) + "点伤害")


# 工具函数,用于判断所有勇士是否都死亡,死亡则游戏结束
def is_alive(heroes):
    for i in heroes:
        if isinstance(i, Hero):
            if i.alive == True:
                return 1
    return 0


# boss线程
class Thread1(threading.Thread):
    def __init__(self, heroes, boss):
        super().__init__()
        self.heroes = heroes
        self.boss = boss

    def run(self):
        time.sleep(1)
        while is_alive(self.heroes) and self.boss.hp > 0:
            for i in self.heroes:
                if isinstance(i, Hero):
                    if random.randint(0, 10) < 8:
                        self.boss.attack(i)
            time.sleep(0.3)  # 这里修改boss的攻击频率
        if (self.boss.hp > 0):
            print("boss获得了胜利")


# 勇士线程
class Thread2(threading.Thread):
    def __init__(self, hero, boss):
        super().__init__()
        self.hero = hero
        self.boss = boss

    def run(self) -> None:
        while self.boss.hp > 0 and self.hero.alive == True:
            self.hero.attack(self.boss)
            time.sleep(0.3)  # 这里修改hero的攻击频率
        if self.boss.hp < 0 and self.hero.alive == True:
            print("勇士" + self.hero.name + "活了下来并取得了胜利!")


if __name__ == '__main__':
    hero1 = Hero("加拿大电鳗", 100, 30)
    hero2 = Hero("金轮", 30, 150)
    hero3 = Hero("中登🐎", 75, 75)
    boss = Boss("西巴老🐎", 2000, 25)
    thread1 = Thread1((hero3, hero2, hero1), boss)
    thread2 = Thread2(hero3, boss)
    thread3 = Thread2(hero2, boss)
    thread4 = Thread2(hero1, boss)
    thread1.start()
    thread4.start()
    thread3.start()
    thread2.start()

