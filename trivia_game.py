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


#printing the title of the game
print(" *****  *****  *****  *       *  *****     ***          ****       **     **    **  ***** ")
print("   *    *   *    *     *     *     *      *   *         *         *  *    * *  * *  * ")
print("   *    *****    *      *   *      *     *******        * ***    ******   *  **  *  ***** ")
print("   *    * *      *       * *       *    *       *       *   *   *      *  *   *  *  * ")
print("   *    *   *  *****      *      ***** *         *      *****  *        * *      *  *****")

#rules for the game
print("""This game has two rounds namely:
Round_1: SITCOM TRIVIA which will include 10 multi choice questions from a sitcom show of player's choice from the three given options.
Round_2: FRIENDS TRIVIA which will include 15 multi choice questions from the most popular show friends.
Rules are as below:
(1)Each correct answer yields a +1 whereas incorrect answer will give you -1. You may skip a question if you want by entering '0' into answer which will lead to no negative marking.
(2)For entering round_2 you need atleast 7 points in round_1.
(3)You have one lifeline to assist you in case you need it in round_1, namely:
1.Change the question - it will change the question.Enter '-1' into the terminal to avail it.
Note that it can be used only once through a single round.
(4)For round_2 you will have two lifelines which can only be used once throughout the round namely:
1.Change the question - it will change the question. Enter '-1' to avail this lifeline.
2.50:50 - It will remove two wrong choices out of the four provided. Enter '5050' to avail this lifeline.
Note - You cannot use the two lifelines in the same question otherwise 0 marks will be awarded.
ENJOY the game:))""")