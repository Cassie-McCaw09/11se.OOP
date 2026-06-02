import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic
    
class Troll(Fighter):
    def __init__(self,name,starting_health,weapon,shield,power):
        super().__init__(name, starting_health, weapon, shield, power)
        self.power = power

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.power


you = Fighter(50,45,80,100,)
wiz = Wizard('The Grey Wizard',55,85,100,50)
troll = Troll('Troll',55,85,100,40)

you.report()
wiz.report()
troll.report()

while True:
    print('You attack the',wiz.name)
    wiz.defend(you.skill_attack())
    wiz.report()
    time.sleep(2)
    print('')
    if wiz.is_dead():
        print('You win')
        break
    print(wiz.name,'attacks you . . .')
    you.defend(wiz.random_attack())
    you.report()
    time.sleep(2)
    if you.is_dead():
        print(wiz.name,'wins')
        break
    print('')

    print('You attack the',troll.name)
    troll.defend(you.skill_attack())
    troll.report
    time.sleep(3)
    print('')
    if wiz.starting_health <=10 : wiz._is_dead
    print ('you win')
    break 
print(wiz.name,'attacks you . . .')
you.defend(wiz.random_attack())
you.report()
time.sleep(2)
if you.is_dead():
        print(wiz.name,'wins')
        break
    print('')