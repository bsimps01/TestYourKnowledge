#Are you a fan of Quizzes?

def question_one():
    response = input("What was the year that Star Wars: A New Hope premiered in theaters? A) 1981 B) 1972 C) 1977 D) 1985 ")

    if response == "C":
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
    else:
        print("Incorrect, the right answer is B) Millenium Falcon.")
        return 0

def question_three():
    response3 = input("Darth Vader's real name is Lando Calrisian. Type T for true or F for false ")

    if response3 == "T":
        print("Sorry that was wrong.")
        return 0
    elif response3 == "F":
        print("Correct!")
        return 1
    else:
        return response3

def question_four():
    response4 = input("What is the name of Luke Skywalker's twin sister? A) Princess Palpatine B) Leslie Calrisian C) Empress Amidala D) Princess Leia ")

    if response4 == "D":
        print("That was right!")
        return 1
    else:
        print("Sorry that was not right.")
        return 0

def question_five():
    response5 = int(input("How many Star Wars films were created that featured Mark Hamil? Including Episode 9, Plese enter a number:"))

    if response5 == 6:
        print("You got it!")
        return 1
    else:
        print("Sorry, the answer was 6.")
        return 0

def question_six():
    response6 = input("What kind of animal is Chewbacca? A) A Wookie B) An Ewok C) Sandperson D) Mandalorian")

    if response6 == "A":
        print("That is correct!")
        return 1
    else:
        print("Sorry that was incorrect.")
        return 0

def question_seven():
    response7 = input("Who has the highest kill count in the Star Wars Universe? A) Darth Vader B) Luke Skywalker C) Princess Leia D) Emperor Palpatine E) Han Solo")
    
    if response7 == "B":
        print("That's right! The Death Star was a big one!")
        return 1
    else:
        print("Sorry that was not correct.")
        return 0

total_score = 0
result = question_one() + question_two() + question_three() + question_four() + question_five() + question_six() + question_seven()
total_score += result
print(total_score)