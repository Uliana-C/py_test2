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

# Описание боя
def fight_to_death(fighter1: Fighter, fighter2: Fighter):
    start_time = time.time()
    log_file = open("logger.txt", "w", encoding="utf-8")
    log_file.write("Начало боя!\n")

    while fighter1.health > 0 and fighter2.health > 0:
        #боец 1 атакует 2
        attack_time = fighter1.attack()
        time.sleep(attack_time)
        current_time = time.time() - start_time
        damage_dealt = fighter2 - fighter1
        log_file.write(f"{current_time:.2f}s: {fighter1.name} атакует {fighter2.name} и наносит {damage_dealt:.2f} урона. "
                       f"{fighter2.name} осталось {fighter2.health:.2f} здоровья.\n")

        if fighter2.health <= 0:
            break

        # боец 2 атакует 1
        attack_time = fighter2.attack()
        time.sleep(attack_time)
        current_time = time.time() - start_time
        damage_dealt = fighter1 - fighter2
        log_file.write(f"{current_time:.2f}s: {fighter2.name} атакует {fighter1.name} и наносит {damage_dealt:.2f} урона. "
                       f"{fighter1.name} осталось {fighter1.health:.2f} здоровья.\n")

    # Определение победит
    if fighter1.health > 0:
        winner = fighter1.name
    else:
        winner = fighter2.name
    log_file.write(f"Бой окончен! Победитель: {winner}\n")
    log_file.close()
# Ввод данных для бойцов
def create_fighter():
    name = input("Введите имя бойца: ")
    health = float(input("Введите здоровье бойца: "))
    damage_min = float(input("Введите минимальный урон бойца: "))
    damage_max = float(input("Введите максимальный урон бойца: "))
    attack_speed_min = float(input("Введите минимальную скорость атаки бойца (в секундах): "))
    attack_speed_max = float(input("Введите максимальную скорость атаки бойца (в секундах): "))
    return Fighter(name, health, [damage_min, damage_max], [attack_speed_min, attack_speed_max])


# Создание бойцов
print("Создание первого бойца:")
fighter1 = create_fighter()

print("\nСоздание второго бойца:")
fighter2 = create_fighter()

# Начало боя
fight_to_death(fighter1, fighter2)