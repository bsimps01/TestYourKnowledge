#Are you a fan of Quizzes?

def question_one():
    response = input("What was the year that Star Wars: A New Hope premiered in theaters? A) 1981 B) 1972 C) 1977 D) 1985")

    if response == "C" or "c":
        print("That's right!")
        return 1
    else: 
        print("Sorry, the correct answer is C) 1977")
        return 0

def question_two():
    response2 = input("What is the name of the spaceship that is piloted by Han Solo and Chewbacca? A) Star Destroyer B) Millenium Falcon C) Lightyear Cruiser D) X-Wing")

    if response2 == "B" or "b":
        print("You got it!")
        return 1
    else:
        print("Incorrect, the right answer is B) Millenium Falcon")
        return 0

def question_three():
    response3 = input("Darth Vader's real name is Lando Calrisian. Type T for true or F for false")

    if response3 == "T" or "t":
        print("Sorry that was wrong")
        return 0
    elif response3 == "F" or "f":
        print("Correct!")
        return 1
    else:
        return response3

def question_four():
    response4 = input("What is the name of Luke Skywalker's twin sister? A) Princess Palpatine B) Leslie Calrisian C) Empress Amidala D) Princess Leia")

    if response4 == "D" or "d":
        print("That was right!")
        return 1
    else:
        print("Sorry that was not right")
        return 0
        
