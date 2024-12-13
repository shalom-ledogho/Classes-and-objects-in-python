#simple inheritance
print('______________________________________________')
class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
    def attack(self,amount):
        print('the monster has attacked')
        print(f'{amount} damage was dealt')
    def move(self,speed):
        self.speed = speed
        #print(f'the monster moves with a speed of {self.speed}')
        
class Shark(Monster):
    def __init__(self,speed,health,energy):
        #####   Monster.__init__(self,health,energy) ######
        super().__init__(health,energy)
        self.speed = speed
    def bite(self):
        print(f'the shark has bitten')
    def move(self):
        print(f'The shark is moving It is moving with a speed of {self.speed} ')

shark = Shark(speed = 120,health = 200,energy = 100)
#shark.move()
#print(f'the shark\'s health is {shark.health}')
#shark.bite()

print('________________________________________')
class Scorpion(Monster):
    def __init__(self,poison_damage,scorpionspeed,scorpionhealth,scorpionenergy):
        super().move(speed = scorpionspeed)
        super().__init__(health = scorpionhealth, energy = scorpionenergy)
        self.poison_damage = poison_damage
    def attack(self):
        print(f'damage dealt was {self.poison_damage} poison damage')
        print(f'The scorpion moves at a speed of {self.speed}')

print(bool(''))
scorpion = Scorpion(poison_damage = 50, scorpionspeed = 30, scorpionhealth = 67, scorpionenergy = 89)       
#scorpion.attack()
print(scorpion.speed)
#scorpion.move(speed = 20)
__name__ = "simple_inheritance"
if __name__ == "simple_inheritance":
    print("hello user")
   
shark.move()
print(scorpion.attack)
    
