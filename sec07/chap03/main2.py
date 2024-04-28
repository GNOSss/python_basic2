class Slime:
    def __init__(self):
        self.hp = 50
        self.attack = 8
        self.defense = 0.2

    def attack_enemy(self, enemy):
        enemy.hp -= self.attack * (1 - enemy.defense)


class FireSlime(Slime):
    def __init__(self):
        super().__init__()
        self.fireAttack = 4

    def attack_enemy(self, enemy):
        total_attack = self.attack + self.fireAttack
        enemy.hp -= total_attack * (1 - enemy.defense)


slime = Slime()   #Slime()클래스를 호출하여 slime이라는 객체를 생성한거 같은데 ?
fire_slime = FireSlime() #FireSlime()클래스를 호출하여 fire_slime이라는 객체를 생성한거 같은데 ?

slime.attack_enemy(fire_slime)  #slime객체에 속한 Slime클래스의 attack_enemy 를 호출하는데 enemy 인스턴스에 fire_slime을 보냄
fire_slime.attack_enemy(slime)  #fire_slime객체에 속한 FireSlime클래스의 attack_enemy 를 호출하는데 enemy 인스턴스에 slime을 보냄

while slime.hp > 0 and fire_slime.hp > 0 :
    if slime.hp > 0 or fire_slime.hp:
        fire_slime.attack_enemy(slime)
        slime.attack_enemy(fire_slime)
        print(f"슬라임 체력 : {slime.hp:.2f} 파이어슬라임 체력 : {fire_slime.hp:.2f}")
    else :
        pass

    if slime.hp <= 0  or fire_slime.hp <= 0:
        print("전투 종료")
        if slime.hp <= 0 :
            print("슬라임이 죽었습니다.", end=(" "))
            print(f"파이어 슬라임 남은 체력 : {fire_slime.hp:.2f}")
        else :
            print("파이어슬라임이 죽었습니다.", end=(" "))
            print(f"슬라임 남은 체력 : {slime.hp:.2f}")

