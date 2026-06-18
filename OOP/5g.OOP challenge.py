# Create a welcome page 
# create user guide/steps 
#try to make welcome page as simple as possible. 
#100 points of stats to be assigned to the character - can be randomised 
import random, time 

print('Welcome') 
time.sleep(3)
print ('Choose your Fighter')
choice = input('Choose your fighter')
time.sleep(2)
print('1. Ninja')
print('2. Warrior')
print('3. Tank')
if choice: ('1. Ninja')
print ('You are now a Ninja!')
if choice: ('2. Warrior')
print('You are now a Warrior!')
if choice: ('3. Tank') 
print ('You are now a Tank!')
time.sleep(3)
choice = input('Choose your rival')
time.sleep(3)
print('1. Troll')
print('2. Wizard')
if choice: ('1.Troll')
print ('You are fighting a Troll, Good luck!')
if choice: ('2. Wizard')
print ('You are battling Wizard, Good Luck!')
time.sleep(3)


#purpose: These are the general variables for fighters, some variables may be added depending on the fighter chosen. 
class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(f"{self.name}: Health: {self.__health}")

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
        print(5,4,3)
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

# purpose: These are the variables for the wizard to keep track of stats throughout the game
class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic
 # purpose: This is the 2nd enemy within the class, there are different variables including all the inherited varibles   
class Troll(Fighter):
    def __init__(self,name,starting_health,weapon,shield,power):
        #pass only the 4 arguements the fighter class expects
        super().__init__(name, starting_health, weapon, shield)
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

        #set power here instead 
        self.power = power

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.power

# pupose: number variables for each corresponding variable. 
you = Fighter('Fighter', 100,50,80)
wiz = Wizard('Wizard',55,85,100,50)
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
    if wiz.starting_health <=10 : wiz._is_dead #still working on this! 
    print ('you win')
    break 
print(wiz.name,'attacks you . . .')
you.defend(wiz.random_attack())
you.report()
time.sleep(2)
if you.is_dead():
    print(wiz.name,'wins')
    