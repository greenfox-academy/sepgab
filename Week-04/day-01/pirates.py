import random

class Pirate:

    def __init__(self):
        self.level_rum = 0
        self.alive = True
        self.passed_out = False

    def drink_some_rum(self):
        if self.alive == True:
            self.level_rum += 1
        else:
            print('He\'s dead.')

    def hows_it_going_mate(self):
        if self.alive == True:
            if self.level_rum < 4:
                print('Pour me anudder!')
            else:
                print('Arghh, I\'ma Pirate. How d\'ya d\'ink its goin?')
                self.passed_out = True
        else:
            print('He\'s dead.')

    def die(self):
        self.alive = False

    def pass_out(self):
        self.passed_out = True

    def brawl(self, other_pirate, parrot=''):
        if other_pirate.alive == True:
            brawl_output = random.randint(0,3)
            if brawl_output == 0:
                self.alive = False
                print('Attacker is dead.')
                parrot.attacker()
            elif brawl_output == 1:
                other_pirate.die()
                print('Attacked pirate is dead.')
                parrot.attacked()
            else:
                self.passed_out = True
                other_pirate.pass_out()
                print('Attacker and attacked pirates are both passed out.')
                parrot.passed_out()
    def get_status(self):
        pass

class Parrot:

    def attacker(self):
        print('The parrot replies: Attacker is dead.')

    def attacked(self):
        print('The parrot replies: Attacked pirate is dead.')

    def passed_out(self):
        print('The parrot replies: Attacker and attacked pirates are both passed out.')

class Ship:
    def __init__(self):
        self.pirate_list = []
        self.captain = 0
        self.pirate_counter = len(self.pirate_list)

    def fill_ship(self):
        self.captain = 1
        self.pirate_gen = random.randint(0,100)
        for i in self.pirate_gen:
            self.pirate_list.append(i)



pirate1 = Pirate()
pirate2 = Pirate()
parrot = Parrot()

pirate1.drink_some_rum()
pirate1.drink_some_rum()
pirate2.drink_some_rum()

pirate1.hows_it_going_mate()

pirate1.drink_some_rum()
pirate1.drink_some_rum()

pirate1.hows_it_going_mate()

pirate1.brawl(pirate2, parrot)
print(pirate1.alive)
print(pirate2.alive)
