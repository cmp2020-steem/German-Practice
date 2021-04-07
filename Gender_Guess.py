import random
import os
import time

def gender_function():
    var = 3
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Gender Guess/streak_gender.txt"
        if var == 2:
            count_file = "../Storage Files/Game Function/Gender Guess/correct_gender.txt"
        if var == 1:
            count_file = "../Storage Files/Game Function/Gender Guess/incorrect_gender.txt"
        os.remove(count_file)
        with open(count_file, "w+") as count_item:
            count_item.write("0")
        count_item.close()
        var = var - 1
    print('Geben Sie "verlassen" ein, um zu verlassen!')
    n = 1
    while n == 1:
        gamble()

def gamble():
    var = random.randint(0, 2)
    if var == 0: #der
        article = "der"
        article_file = "../Storage Files/Words/der.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Gender Guess/incorrect_der.txt"
    if var == 1: #das
        article = "das"
        article_file = "../Storage Files/Words/das.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Gender Guess/incorrect_das.txt"
    if var == 2: #die
        article = "die"
        article_file = "../Storage Files/Words/die.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Gender Guess/incorrect_die.txt"
    build_the_list(article, article_file, incorrect_answer_file)

def build_the_list(article, article_file, incorrect_answer_file):
    article_list = []
    with open(article_file, "r+") as file:
        list_raw = list(file)
        for list_word in list_raw:
            article_list.append(list_word.rstrip())
    file.close()
    with open(incorrect_answer_file, "r+") as incorrect_file:
        incorrect_list_raw = list(incorrect_file)
        for incorrect_list_word in incorrect_list_raw:
            article_list.append(incorrect_list_word.rstrip())
    incorrect_file.close()
    pick_the_word(article, article_list, article_file, incorrect_answer_file)

def pick_the_word(article, article_list, article_file, incorrect_answer_file):
    word = article_list[random.randint(0, len(article_list) - 1)]
    print(word)
    answer = input("der, das, oder die?: ")
    if answer.lower() == article:
        print("Richtig!")
        check_incorrect_file(incorrect_answer_file, word)
        correct_count()
    if answer.lower() != article and answer.lower() not in ("quit", "q", "verlassen"):
        print("Es tut mir leid! Das ist nicht richtig!")
        add_to_incorrect_file(incorrect_answer_file, word)
        incorrect_count()
    if answer.lower() in ("quit", "q", "verlassen", "v"):
        end_of_game()
        quit()
    n = 1


def check_incorrect_file(incorrect_answer_file, word):
    incorrect_list = []
    with open(incorrect_answer_file, "r+") as incorrect_file:
        incorrect_list_raw = list(incorrect_file)
        for incorrect_list_word in incorrect_list_raw:
            incorrect_list.append(incorrect_list_word.rstrip())
        incorrect_file.close()
    if word in incorrect_list:
        incorrect_list.remove(word)
        os.remove(incorrect_answer_file)
        with open(incorrect_answer_file, 'w+') as incorrect_file:
            for item in incorrect_list:
                incorrect_file.write("%s\n" % item)

def add_to_incorrect_file(incorrect_answer_file, word):
    with open(incorrect_answer_file, "a+") as incorrect_file:
        incorrect_file.write(word + "\n")
    incorrect_file.close()

def correct_count():
    var = 3
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Gender Guess/streak_gender.txt"
            print("Streak: ")
        if var == 2:
            count_file = "../Storage Files/Game Function/Gender Guess/correct_gender.txt"
            print("Correct: ")
        if var == 1:
            count_file = "../Storage Files/Game Function/Gender Guess/incorrect_gender.txt"
            print("Incorrect: ")
        with open(count_file, "r+") as count_item:
            count_list = list(count_item)
        count_item.close()
        count = int(count_list[0])
        if var == 1:
            print(count)
        if var > 1:
            count = count + 1
            print(count)
            os.remove(count_file)
            with open(count_file, "w+") as count_item:
                count_item.write(str(count))
            count_item.close()
        var = var - 1

def incorrect_count():
    var = 3
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Gender Guess/streak_gender.txt"
            print("Streak: ")
            count = 0
            os.remove(count_file)
            with open(count_file, "w+") as count_item:
                count_item.write(str(count))
            count_item.close()
            print(count)
        if var == 2:
            count_file = "../Storage Files/Game Function/Gender Guess/correct_gender.txt"
            print("Correct: ")
            with open(count_file, "r+") as count_item:
                count_list = list(count_item)
            count_item.close()
            count = int(count_list[0])
            print(count)
        if var == 1:
            count_file = "../Storage Files/Game Function/Gender Guess/incorrect_gender.txt"
            print("Incorrect: ")
            with open(count_file, "r+") as count_item:
                count_list = list(count_item)
            count_item.close()
            count = int(count_list[0]) + 1
            count_item.close()
            os.remove(count_file)
            with open(count_file, "w+") as count_item:
                count_item.write(str(count))
            count_item.close()
            print(count)
        var = var - 1

def end_of_game():
    var = 3
    with open("../Storage Files/Game Function/Gender Guess/highscore_gender.txt") as file:
        highscore_list = [int(x) for x in file.read().split()]
    file.close()
    os.remove("../Storage Files/Game Function/Gender Guess/highscore_gender.txt")
    print("-----------------------------------")
    while var > 0:
        time.sleep(1)
        if var == 3:
            count_file = "../Storage Files/Game Function/Gender Guess/streak_gender.txt"
            highscore = highscore_list[0]
        if var == 2:
            count_file = "../Storage Files/Game Function/Gender Guess/correct_gender.txt"
            highscore = highscore_list[0]
        if var == 1:
            count_file = "../Storage Files/Game Function/Gender Guess/incorrect_gender.txt"
            highscore = -1
        with open(count_file, "r+") as count_item:
            count_list = list(count_item)
        count_item.close()
        count = int(count_list[0])
        if count > highscore and highscore != -1:
            highscore_list.remove(highscore)
            highscore_list.append(count)
            if var == 3:
                print("Final Streak: ", count)
            if var == 2:
                print("Final Correct: ", count)
            print("New high score!")
            print("-----------------------------------")
        if highscore > count:
            highscore_list.remove(highscore)
            highscore_list.append(highscore)
            if var == 3:
                print("Final Streak: ", count)
            if var == 2:
                print("Final Correct: ", count)
            print("High score: ", highscore)
            print("-----------------------------------")
        if highscore == -1:
            print("Final Incorrect: ", count)
            print("-----------------------------------")

        var = var - 1
    with open("../Storage Files/Game Function/Gender Guess/highscore_gender.txt", "a+") as file:
        x = 0
        while x <= len(highscore_list)-1:
            file.write("{}{}".format(highscore_list[x], "\n"))
            x = x + 1
    file.close()
    time.sleep(1)
    print("Danke fürs Spielen!")
    input("Geben Sie etwas ein, um es zu beenden")
    n = 0
    quit()

# Code
gender_function()