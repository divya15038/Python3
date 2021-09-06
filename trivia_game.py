class Player:
    #initializes the player name and the category for round 1
    def __init__(self, name, category, total1 = 0):
        self.name = name
        self.category = category
        self.total = total1
        print("Let us begin with the first round!")
    
    #increments the score by one when question answered correctly
    def incr(self):
        self.total += 1

    #decrements the score by 1 when question answered incorrectly
    def decr(self):
        self.total -= 1