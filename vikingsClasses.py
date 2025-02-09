
# Soldier
import random as rn
class Soldier:

    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health-=damage

# Vikingclass So


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
    def receiveDamage(self, damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"    




# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        Saxon=rn.choice(self.saxonArmy)
        Viking=rn.choice(self.vikingArmy)
        Saxon.receiveDamage(Viking.strength)
        if Saxon.health<=0:
            self.saxonArmy.remove(Saxon)
            return "A Saxon has died in combat" 
        else:
            return f"A Saxon has received {damage} points of damage"
    def saxonAttack(self):
        Saxon=rn.choice(self.saxonArmy)
        Viking=rn.choice(self.vikingArmy)
        Viking.receiveDamage(Saxon.strength)
        if Viking.health<=0:
            self.vikingArmy.remove(Viking)
            return f"{Viking.name} has died in act of combat"
        else:
            return f"{Viking.name} has received {Saxon.strength} points of damage"
    def showStatus(self):
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.saxonArmy)==1 and len(self.vikingArmy)==1:
            return "Vikings and Saxons are still in the thick of battle."
