#Learning Intentions
#1. Create a defend method that helps you repel an attack
#2. Create a loop which simulates a fight and declares a winner
#3. Test the game 

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ 'Health '+ str (self.health))

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack Power:', attack_power)
        return attack_power
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health = self.health - damage
            print('Damage:', damage)
        else:
            print('No Damage')



you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)


you.report()
troll.report()

while True:
    print('You attack the troll')
    troll.defend (you.random_attack())
    troll.report()
    time.sleep(3)
    print('')
    if troll.heatlh <= 0:
        print('You win')
        break
    print('The troll attack you . . .')
    you.defend (troll.random_attack())
    you.report()
    time.sleep(3)
    if you.health <= 0:
        print ('The troll wins')
        break
    print('')
