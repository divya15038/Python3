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

    #used for declaring result for round_1
    def qualify_round_1(self):
        if self.total >= 7:
            print("Congratulations! You got in round 2.")
            print("Your score is {}".format(self.total))
            self.total = 0
        else:
            print("Unfortunately, you weren't able to qualify for round_2. Your score is {}".format(self.total))
            print("Still, you participated and paricipation is the first step towards learning.")
            print("Thanks for participating!Better luck next time:))")
            exit()
    
    #used for declaring result for round_2
    def qualify_round_2(self):
        if self.total >= 12:
            print("Congratulations! Yoh have scored {} points.".format(self.total))
            print("You really are 'THE BIGGEST SITCOM FAN EVER'!!!")
        else:
            print("Congratulations on finishing this TRIVIA GAME. I hope you enjoyed it. You scored a total of {} points.".format(self.total))
            print("You really are 'A FAN'!!")
        print("Thankyou for playing:))")