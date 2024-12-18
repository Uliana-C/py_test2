import random
import time

class Fighter:
    def __init__(self, name: str, health: float, damage: list[float, float], attack_speed: list[float, float]):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed

#Метод получения урона от бойца
    def __sub__(self, other):
        damage_taken = random.uniform(other.damage[0], other.damage[1])
        self.health -= damage_taken
        return damage_taken

#Возвращает время до следующей атаки
    def attack(self):
        return random.uniform(self.attack_speed[0], self.attack_speed[1])

