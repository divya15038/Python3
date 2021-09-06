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

#Ask the player for name and choice of show for round_1
category = {1: "The Big Bang Theory", 2: "Schitt's Creek", 3: "Modern Family"}
name = input('Enter your name: ')
print("""You have the following choices for round1:{}""".format(category))
tv_show = int(input('Enter number for sitcom for round_1: '))

#Checking for the valid entry of number for category
if tv_show in category:
    print("{} tv_show selected for round_1 by {}.".format(category[tv_show], name))
else:
    print("Invalid number.Please enter a valid number out of the given categories.")

#Initializing player1 object of class 'Player'
player_1 = Player(name, tv_show)

#Big Bang Theory Trivia
big_bang_theory_questions = {"What does Sheldon's mom call him?": ['1.Sheldon', '2.Pumpkin', '3.Shelly', '4.Doc'], "What breed of dog does Raj have?": ['1.Cocker Spaniel', '2.Golden Retriever', '3.Maltese', '4.Yorkshire Terrier'], "Who is the only member of the cast to hold a PhD in real life": ['1.Jim Parsons', '2.Johnny Galecki', '3.Mayim Bialik', '4.Kaley Cuoco'], "What astronaut nickname was Howard given by his space friends": ['1.Rocket Man', '2.Howie', '3.Froot Loops', '4.Big Guy'], "What is the name of the science show host played by Bob Newhart that Sheldon and Leonard love so much?": ['1.Professor Proton', '2.Dr.DNA', '3.Mr.Microbe', '4.The Sultan of Science'], "Where did Amy get her undergraduate degree?": ['1.Standford', '2.Yale', '3.MIT', '4.Harvard'], "What apartment do Penny and Leonard live in?": ['1.4B', '2.3B', '3.3A', '4.4A'], "Who was once engaged to a Saudi prince?": ['1.Penny', '2.Bernadette', '3.Amy', '4.Raj'], "Who officiates Sheldon and Amy's wedding?": ['1.Will Weathon', '2.Leonard', '3.Mark Hamill', '4.Raj'], "Where do Sheldon, Amy, Raj, Howard and Leonard work?": ['1.Caltech', '2.UCLA', '3.USC', '4.Cal Poly'], "How did Sheldon and Amy meet?": ['1.Online Dating', '2.Through Leonard', '3.Through Penny', '4.At Caltech'], "Where is Sheldon originally from?": ['Texas', 'LA', 'Oklohoma', 'Pennsylvania']}
big_bang_theory_answers = {"What does Sheldon's mom call him?": 3, "What breed of dog does Raj have?": 4, "Who is the only member of the cast to hold a PhD in real life": 3, "What astronaut nickname was Howard given by his space friends": 3, "What is the name of the science show host played by Bob Newhart that Sheldon and Leonard love so much?": 1, "Where did Amy get her undergraduate degree?": 4, "What apartment do Penny and Leonard live in?": 4, "Who was once engaged to a Saudi prince?": 3, "Who officiates Sheldon and Amy's wedding?": 3, "Where do Sheldon, Amy, Raj, Howard and Leonard work?": 1, "How did Sheldon and Amy meet?": 1, "Where is Sheldon originally from?": 1}

count = 0
lifeline = True
#Checking for category for round_1
if tv_show == 1:
    for question in big_bang_theory_questions:
        if count < 10:
            print("Question:")
            print(question)
            print(big_bang_theory_questions[question])
            answer = input('Answer: ')
            #checking for correct answer
            if int(answer) == big_bang_theory_answers[question]:
                player_1.incr()
                print("Congratulations! This is the correct answer.")
                count += 1
            #Skipping question marks awarded =0
            elif answer == '0':
                print("Skipping the present question.")
                count += 1
                continue
            #flipping the question
            elif answer == '-1' and lifeline == True:
                print("Changing the question")
                lifeline = False
                continue
            #checking that the lifeline is used only once
            elif answer == '-1' and lifeline == False:
                print("You can use the lifeline only once.So you'll be awarded 0 marks for this question.")
                count += 1
                continue
            #checking for incorrect answer
            else:
                print("Unfortunately, your answer is incorrect:(( ")
                player_1.decr()
                count += 1
    #giving the final result
    player_1.qualify_round_1()


#Schitt's Creek Trivia
schitts_creek_questions = {"What dish does Moira Rose try to cook in second season's 'Family Dinner' episode?": ['1.Meatloaf', '2.Enchiladas', '3.Lasagna', '4.Brocolli Casserole'], "David meets the love of his life Patrick when..": ['1.Trying to get licensing for his apothecary shop', '2.Going on a turkey hunt', '3.Patrick serenades him', '4.On a road trip'], "Alexis meets Mutt while doing community service for...": ['1.Possession', '2.Grand Theft Auto', '3.Driving Under the Influence', '4.Jaywalking'], "Johnny Rose was a little worried by the welcome sign for Schitt's Creek. What sign did Roland add to solve the problem?": ['1.We believe in family values!', "2.Don't Worry. It's his sister!", "3.Spelled with a 'C'!", "4.We're flush with all kinds of crap!"], "What hunting does David go on with Stevie?": ['1.Tiger hunting', '2.Chicken hunting', '3.Ostrich hunting', '4.Turkey hunting'], "What is the name of the female music group in Schitt's Creek?": ['1.Jazzagals', '2.Popstar Pipettes', '3.Blues Birds', '4.Songstresses'], "Twyla works in which cafe?": ['1.Cafe Creek', '2.Cafe Tropical', '3.Starbucks', '4.Rose Cafe'], "In what commercial does Moira Rose star after coming to Schitt's Creek": ['1.Canned lasagna', '2.Fruit Wine', '3.Bedazzled bidets', '4.Organic Mascara'], "Which council member is married to Gwen": ['1.Ronnie', '2.Ray', '3.Roland', '4.Bob'], "Why did Jhonny Rose purchase the Schitt's Creek town": ['1.As a wedding gift for Moira', '2.As a joke for Alexis', '3.As a joke for David', '4.As an investment'], "On David's wedding day, what does Alexis wear?": ['1.A wedding dress', "2.Moira's Red carpet gown", '3.A black dress', '4.A golden gown']}
schitts_creek_answers = {"What dish does Moira Rose try to cook in second season's 'Family Dinner' episode?": 2, "David meets the love of his life Patrick when..": 1, "Alexis meets Mutt while doing community service for...": 3, "Johnny Rose was a little worried by the welcome sign for Schitt's Creek. What sign did Roland add to solve the problem?": 2, "What hunting does David go on with Stevie?": 4, "What is the name of the female music group in Schitt's Creek?": 1, "Twyla works in which cafe?": 2, "In what commercial does Moira Rose star after coming to Schitt's Creek": 2, "Which council member is married to Gwen": 4, "Why did Jhonny Rose purchase the Schitt's Creek town": 3, "On David's wedding day, what does Alexis wear?": 1}


#Checking for category for round_2
if tv_show == 2:
    for question in schitts_creek_questions:
        if count < 10:
            print("Question:")
            print(question)
            print(schitts_creek_questions[question])
            answer = input('Answer: ')
            #checking for correct answer
            if int(answer) == schitts_creek_answers[question]:
                player_1.incr()
                print("Congratulations! This is the correct answer.")
                count += 1
            #Skipping question marks awarded =0
            elif answer == '0':
                print("Skipping the present question.")
                count += 1
                continue
            #flipping the question
            elif answer == '-1' and lifeline == True:
                print("Changing the question")
                lifeline = False
                continue
            #checking that the lifeline is used only once
            elif answer == '-1' and lifeline == False:
                print("You can use the lifeline only once.So you'll be awarded 0 marks for this question.")
                count += 1
                continue
            #checking for incorrect answer
            else:
                print("Unfortunately, your answer is incorrect:(( ")
                player_1.decr()
                count += 1
        #giving the final result
    player_1.qualify_round_1()