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

class Hero(Character):
    def __init__(self, name, life, level, special_skill):
        super().__init__(name, life, level)
        self.__special_skill = special_skill

    def get_special_skill(self):
        return self.__special_skill
    
class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
