#Are you a fan of Quizzes?

def question_one():
    response = input("What was the year that Star Wars: A New Hope premiered in theaters? A) 1981 B) 1972 C) 1977 D) 1985 ")

    if response == "C":
        print("That's right!")
        return 1
    elif response == "c":
        print("That's right!")
        return 1
    else: 
        print("Sorry, the correct answer is C) 1977")
        return 0

def question_two():
    response2 = input("What is the name of the spaceship that is piloted by Han Solo and Chewbacca? A) Star Destroyer B) Millenium Falcon C) Lightyear Cruiser D) X-Wing ")

    if response2 == "B":
        print("You got it!")
        return 1
    elif response2 == "b":
        print("You got it!")
        return 1
    else:
        print("Incorrect, the right answer is B) Millenium Falcon.")
        return 0

def question_three():
    response3 = input("Darth Vader's real name is Lando Calrisian. Type T for true or F for false ")

    if response3 == "T":
        print("Sorry that was wrong.")
        return 0
    elif response3 == "t":
        print("Sorry that was wrong.")
        return 0
    elif response3 == "F":
        print("Correct!")
        return 1
    elif response3 == "f":
        print("Correct!")
        return 1
    else:
        return response3

def question_four():
    response4 = input("What is the name of Luke Skywalker's twin sister? A) Princess Palpatine B) Leslie Calrisian C) Empress Amidala D) Princess Leia ")

    if response4 == "D":
        print("That was right!")
        return 1
    elif response4 == "d":
        print("That was right!")
        return 1
    else:
        print("Sorry that was not right.")
        return 0

def question_five():
    response5 = int(input("How many Star Wars films were created that featured Mark Hamil? Including Episode 9, Plese enter a number: "))

    if response5 == 6:
        print("You got it!")
        return 1
    else:
        print("Sorry, the answer was 6.")
        return 0

def question_six():
    response6 = input("What kind of animal is Chewbacca? A) A Wookie B) An Ewok C) Sandperson D) Mandalorian ")

    if response6 == "A":
        print("That is correct!")
        return 1
    elif response6 == "a":
        print("That is correct!")
        return 1
    else:
        print("Sorry that was incorrect.")
        return 0

def question_seven():
    response7 = input("What was the name of the space station that was used to destroy planets? A) Death Destroyer B) Death Star C) Star Killer D) Death Seeker E) Grim Celestial ")
    
    if response7 == "B":
        print("That's right! The Death Star was a big one!")
        return 1
    if response7 == "b":
        print("That's right! The Death Star was a big one!")
        return 1
    else:
        print("Sorry that was not correct.")
        return 0

total_score = 0
result = question_one() + question_two() + question_three() + question_four() + question_five() + question_six() + question_seven()
total_score += result
print(total_score)

def final_score():
    if total_score == 7:
        print("Great job! You got them all right!")
    elif total_score == 6:
        print("Nice work, you got 6 right!")
    elif total_score == 5:
        print("You got 5 out of 7 right, not bad")
    elif total_score == 4:
        print("You got 4 out of 7, not bad.")
    elif total_score == 3:
        print("3 out of 7, better luck next time")
    elif total_score == 2:
        print("Ouch. 2 out of 7, not the greatest.")
    elif total_score == 1:
        print("Dang, the force is not strong with you. 1 out of 7")
    else:
        print("0 out of 7, do or do not, there is no try")

def game_over():
    game = input("Would you like to play again? Y to continue or N for no: ")

    if game == "Y":
        question_one()
        question_two()
        question_three()
        question_four()
        question_five()
        question_six()
        question_seven()
        final_score()
        game_over()
    elif game == "N":
        exit()

final_score()
game_over()