import random

class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_attack(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and gave {damage} of damage!")
    


class Hero(Character):
    def __init__(self, name, life, level, special_skill):
        super().__init__(name, life, level)
        self.__special_skill = special_skill

    def get_special_skill(self):
        return self.__special_skill
    def show_details(self):
        return f"{super().show_details()}\nSpecial Skill: {self.get_special_skill()}\n"
    def use_special_skill(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_attack(damage)
        print(f"{self.get_name()} used special skill {self.get_special_skill()} on {target.get_name()} and gave {damage} of damage!")

    
class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}"
    
class Game:
    def __init__(self):
        self.hero = Hero(name="Birdman", life=100, level=5, special_skill="Fly")
        self.enemy = Enemy(name="Ekans", life=70, level=4, type="Poisonous")
    
    def starting_battle(self):
        print("Battle has started!")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nCharacters Details")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Press Enter to attack...")
            choice = input("Choose (1 - Normal Attack, 2 - Special Skill):")
            
            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.use_special_skill(self.enemy)
            else:
                print("Invalid choice. Try again")

            if self.enemy.get_life() > 0:
                self.enemy.attack(self.hero)


        if self.hero.get_life() > 0:
            print("\nCongratulations, you won the battle!")
        else:
            print("\nOh no, you lost the battle!")



game = Game()
game.starting_battle()