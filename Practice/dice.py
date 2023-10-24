class Dice:
    def roll(self):
        import random


        dice = (1, 2, 3, 4, 5, 6)

        first_dice = random.choice(dice)
        second_dice = random.choice(dice)

        print(f'({first_dice}, {second_dice})')
        

dice = Dice()
dice.roll()

