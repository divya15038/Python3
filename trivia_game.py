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

#modern family trivia for round_1
modern_family_questions = {"How may Emmys did Modern Family win and was nominated for?": ['1.22, 82', '2.20, 40', '3.16, 30', '4.14, 40'], "What's the name of Gloria's and Jay's son?": ['1.Manny', '2.Joe', '3.Luke', '4.Jose'], "What kind of company does Jay own?": ['1.sports equipments', '2.school tetxbooks', '3.closets', '4.pipe manufacturing'], "What is Cameron's alter ego clown's name?": ['1.Chuckles', '2.Tizbo', '3.Franky','4.Fizbo'], "Who's afraid of clowns after they found one dead in the woods?": ['1.Phil', '2.Manny', '3.Mitchell', '4.Jay'], "What friend of Jay's does Mitchell say was gay?": ['1.Shortie', '2.LeMicheal', '3.Leftie', '4.Ludwig'], "What is Phil's role play name on Valentine's Day?": [ '1.Cliff Dixon', '2.Clive Bixy','3.Chuck Smith', '4.Harry Stone'],"Who was Luke's first girlfriend?": ['1.Simone', '2.Rhonda', '3.Becca', '4.Janice'], "What number did Manny wear when he played football?": ['1.92', '2.99', '3.81', '4.75'], "How may moves did it take Manny to beat Jay in chess?": ['1.7', '2.2', '3.4', '4.5'], "What elementary school do Manny and Luke go to?": ['1.McKinley', '2.Franklin', '3.Grant', '4.Walgrove']}
modern_family_answers = {"How may Emmys did Modern Family win and was nominated for?": 1, "What's the name of Gloria's and Jay's son?": 2, "What kind of company does Jay own?": 3, "What is Cameron's alter ego clown's name?": 4, "Who's afraid of clowns after they found one dead in the woods?": 1, "What friend of Jay's does Mitchell say was gay?": 1, "What is Phil's role play name on Valentine's Day?": 2, "Who was Luke's first girlfriend?": 4, "What number did Manny wear when he played football?":1, "How may moves did it take Manny to beat Jay in chess?": 3, "What elementary school do Manny and Luke go to?": 4}

#Checking for category for round_1
if tv_show == 3:
    for question in modern_family_questions:
        if count < 10:
            print("Question:")
            print(question)
            print(modern_family_questions[question])
            answer = input('Answer: ')
            #checking for correct answer
            if int(answer) == modern_family_answers[question]:
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

print("""Welcom to round_2
Just as a reminder.This round has 15 multi choice questions.For each correct answer you get +1 and for incorrect -1.
You can skip a question by pressing 0.
Also you can use two lifelines:
(1)Change the question: Press '-1' to avial it.
(2)50:50 : Press '5050' to avail it.
ALL THE BEST ;)) """)
#Round 2 begins

#friends trivia 
friends_trivia_questions = {"What is the name of Rachel's hairless cat?": ['1.Mrs.Cottontail', '2.Fluffy', '3.Mrs.Whiskerson', '4.Miss Kitty'], "Who got stuck in a pair of leather pants?": ['1.Ross', '2.Joey', '3.Chandler', '4.Monica'], "What is the name of Phoebe's alter ego?": ['1.Monana Spratt', '2.Regina Phalange', '3.Felula Jane', '4.Jemima Puddleduck'], "Who says the last line of the series?": ['1.Joey', '2.Ross', '3.Monica', '4.Chandler'], "What kind of animal is Joey's friend 'HUGSY'?": ['1.Puppy', '2.Panda', '3. Penguin', '4.Cat'], "Where did Rachel, Monica and Ross go to high school?": ['1.Lincoln High', '2.Washington High', '3.Marymount High', '4.Brooklyn High'], "What color is the couch in Central Perk?": ['1.Brown', '2.Black', '3.Orange', '4.Red'], "How many categories of towels does Monica have?": ['1.10', '2.11', '3.12', '4.9'], "Where do friends go on holiday for Ross's boring palaeontology conference?": ['1.Minsk', '2.Cancum','3.Barbados', '4.Yemen'], "What is the name of Joey's Agent?": ['1.Estella', '2.Edith', '3.Erin', '4.Erica'], "What kind of uniform does Joey wear to Monica and Chandler's wedding?": ['1.Police', '2.Fireman', '3.Navy', '4.Army'], "How many babies are born during the show's 10 seasons?": ['1.6', '2.7', '3.3', '4.5'], "What is Chandler's middle name?": ['1.Marcel', '2.Marice', '3.Muriel', '4.Marine'], "What was Rachel's childhood dog called?": ['1.LaPoo', '2.Marcel', '3.Bo Bo', '4.Chi Chi'], "What is the name of Joey, Ross and Chandler's favorite basketball team?": ['1.The Yankees', '2.The Knicks', '3.The Lakers', '4.The Celtics'], "What did Monica and Chandler name their kids?": ['1.Jake and Alice', '2.Jack and Erica', '3.John and Alice', '4.Johna and Emma']}
friends_trivia_answers = {"What is the name of Rachel's hairless cat?": 3, "Who got stuck in a pair of leather pants?": 1, "What is the name of Phoebe's alter ego?": 2, "Who says the last line of the series?": 4, "What kind of animal is Joey's friend 'HUGSY'?": 3, "Where did Rachel, Monica and Ross go to high school?": 1, "What color is the couch in Central Perk?": 3, "How many categories of towels does Monica have?": 2, "Where do friends go on holiday for Ross's boring palaeontology conference?": 3, "What is the name of Joey's Agent?": 1, "What kind of uniform does Joey wear to Monica and Chandler's wedding?": 4, "How many babies are born during the show's 10 seasons?": 2, "What is Chandler's middle name?": 3, "What was Rachel's childhood dog called?": 1, "What is the name of Joey, Ross and Chandler's favorite basketball team?": 2, "What did Monica and Chandler name their kids?": 2}
friends_trivia_5050 = {"What is the name of Rachel's hairless cat?": ['1.Fluffy', '3.Mrs.Whiskerson'], "Who got stuck in a pair of leather pants?": ['1.Ross', '3.Chandler'], "What is the name of Phoebe's alter ego?": ['2.Regina Phalange', '3.Felula Jane'], "Who says the last line of the series?": ['1.Joey', '4.Chandler'], "What kind of animal is Joey's friend 'HUGSY'?": ['2.Panda', '3.Penguin'], "Where did Rachel, Monica and Ross go to high school?": ['1.Lincoln High', '2.Washington High'], "What color is the couch in Central Perk?": ['1.Brown', '3.Orange'], "How many categories of towels does Monica have?": ['1.10', '2.11'], "Where do friends go on holiday for Ross's boring palaeontology conference?": ['3.Barbados', '4.Yemen'], "What is the name of Joey's Agent?":['1.Estella', '2.Edith'], "What kind of uniform does Joey wear to Monica and Chandler's wedding?": ['1.Police', '4.Army'], "How many babies are born during the show's 10 seasons?": ['1.6', '2.7'], "What is Chandler's middle name?": ['1.Marcel', '3.Muriel'], "What was Rachel's childhood dog called?": ['1.LaPoo', '3.Bo Bo'], "What is the name of Joey, Ross and Chandler's favorite basketball team?": ['1.The Yankees', '2.The Knicks'], "What did Monica and Chandler name their kids?": ['2.Jack and Erica', '3.John and Alice']}


counter = 0
counter_cpy = 0
lifeline1 = True
lifeline = True
for question in friends_trivia_questions:
    if counter < 15:
        print("Question:")
        print(question)
        print(friends_trivia_questions[question])
        answer = input('Answer: ')
        #checking for correct answer
        if int(answer) == friends_trivia_answers[question]:
            player_1.incr()
            print("Congratulations! This is the correct answer.")
            counter += 1
        #Skipping question marks awarded =0
        elif answer == '0':
            print("Skipping the present question.")
            counter += 1
            continue
        #flipping the question
        elif answer == '-1' and lifeline == True:
            print("Changing the question")
            counter_cpy = counter
            lifeline = False
            continue
        #checking that the lifeline is used only once
        elif answer == '-1' and lifeline == False:
            print("You can use the lifeline only once.So you'll be awarded 0 marks for this question.")
            counter += 1
            continue
        #checking if lifeline 5050 is only used once
        elif answer == '5050' and lifeline1 == False:
            print("You can use this lifeline only once and hence will be awarded no points.")
            counter += 1
            continue
        elif answer == '5050' and counter == counter_cpy and lifeline == False:
            print("You can use only one lifeline in a single question and hence will be awarded no points.")
            counter += 1
        #checking for lifeline 5050
        elif answer == '5050' and lifeline1 == True:    
            print("Activating lifeline: '50:50'. Your options are:")
            print(friends_trivia_5050[question])
            lifeline1 = False
            answer2 = input('Answer: ')
            if int(answer2) == friends_trivia_answers[question]:
                player_1.incr()
                print("Congratulations! This is the correct answer.")
                counter += 1
            #Skipping question marks awarded =0
            elif answer2 == '0':
                print("Skipping the present question.")
                counter += 1
                continue
            elif answer2 == '-1':
                print("You can use only one lifeline in a single question and hence no point will be awarded.")
                count += 1
            else:
                print("Unfortunately, your answer is incorrect:(( ")
                player_1.decr()
                counter += 1
        else:
            print("Unfortunately, your answer is incorrect:(( ")
            player_1.decr()
            counter += 1
#giving the final result
player_1.qualify_round_2()