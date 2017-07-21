import random


class Creature:
    # level
    # name
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creater {} of level {}".format(
            self.name, self.level
        )


class Wizard(Creature):
    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("You roll {} against {}'s {}".format(
            my_roll, creature.name, creature_roll
        ))

        if my_roll >= creature_roll:
            print('{} defeats {}'.format(self.name, creature.name))
            return True
        else:
            print('{} loses...'.format(self.name))
            return False
