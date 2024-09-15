class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def showInfo(self):
        print(f"name:{self.name}")
        print(f"hp:{self.hp}")

    def sethp(self, newhp):
        self.hp = newhp

    def gethp(self):
        return self.hp

player1 = Player("human")
player1.sethp(80)
print(player1.gethp())
player1.showInfo()
player2 = Player("elf")
player2.showInfo()