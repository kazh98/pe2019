class Dice(object):
    def __init__(self, labels):
        self.stat = labels

    def roll_e(self):
        self.stat[0], self.stat[2], self.stat[5], self.stat[3] = self.stat[3], self.stat[0], self.stat[2], self.stat[5]

    def roll_w(self):
        self.stat[0], self.stat[2], self.stat[5], self.stat[3] = self.stat[2], self.stat[5], self.stat[3], self.stat[0]

    def roll_n(self):
        self.stat[0], self.stat[1], self.stat[5], self.stat[4] = self.stat[1], self.stat[5], self.stat[4], self.stat[0]

    def roll_s(self):
        self.stat[0], self.stat[1], self.stat[5], self.stat[4] = self.stat[4], self.stat[0], self.stat[1], self.stat[5]

    def get_top(self):
        return self.stat[0]


dice = Dice(input().split())
commands = input()
for command in commands:
    if command == "E":
        dice.roll_e()
    elif command == "W":
        dice.roll_w()
    elif command == "N":
        dice.roll_n()
    elif command == "S":
        dice.roll_s()
print(dice.get_top())
