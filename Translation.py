import random
import os
import time

def translation():
    var = 3
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Translation/streak_trans.txt"
        if var == 2:
            count_file = "../Storage Files/Game Function/Translation/correct_trans.txt"
        if var == 1:
            count_file = "../Storage Files/Game Function/Translation/incorrect_trans.txt"
        os.remove(count_file)
        with open(count_file, "w+") as count_item:
            count_item.write("0")
        count_item.close()
        var = var - 1
    answer = input("(1) Deutsch oder (2) Englisch?: ")
    if answer == "1" or answer.lower() == "deutsch":
        language = 1
    if answer == "2" or answer.lower() == "englisch":
        language = 2
    print('Geben Sie "verlassen" ein, um zu verlassen!')
    n = 1
    while n == 1:
        gamble(language)

def gamble(language):
    var = random.randint(0, 6)
    if var == 0: #der
        article = "der"
        article_file = "../Storage Files/Words/der.txt"
        article_eng_file = "../Storage Files/Words/der_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_der_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_der_eng_trans.txt"
    if var == 1: #das
        article = "das"
        article_file = "../Storage Files/Words/das.txt"
        article_eng_file = "../Storage Files/Words/das_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_das_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_das_eng_trans.txt"
    if var == 2: #die
        article = "die"
        article_file = "../Storage Files/Words/die.txt"
        article_eng_file = "../Storage Files/Words/die_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_die_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_die_eng_trans.txt"
    if var == 3: #verb
        article = "verb"
        article_file = "../Storage Files/Words/verb.txt"
        article_eng_file = "../Storage Files/Words/verb_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_verb_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_verb_eng_trans.txt"
    if var == 4: #adjective
        article = "adjective"
        article_file = "../Storage Files/Words/adj.txt"
        article_eng_file = "../Storage Files/Words/adj_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_adj_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_adj_eng_trans.txt"
    if var == 5: #adverb
        article = "adverb"
        article_file = "../Storage Files/Words/adv.txt"
        article_eng_file = "../Storage Files/Words/adv_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_adv_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_adv_eng_trans.txt"
    if var == 6: #phrases
        article = "phrase"
        article_file = "../Storage Files/Words/phrases.txt"
        article_eng_file = "../Storage Files/Words/phrases_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_phrases_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_phrases_eng_trans.txt"
    if var == 7: #prepositions
        article = "preposition"
        article_file = "../Storage Files/Words/prep.txt"
        article_eng_file = "../Storage Files/Words/prep_eng.txt"
        incorrect_answer_file = "../Storage Files/Game Function/Translation/incorrect_prep_trans.txt"
        incorrect_eng_answer_file = "../Storage Files/Game Function/Translation/incorrect_prep_eng_trans.txt"
    build_the_list(article, article_file, article_eng_file, incorrect_answer_file, incorrect_eng_answer_file, language)


def build_the_list(article, article_file, article_eng_file, incorrect_answer_file, incorrect_eng_answer_file, language):
    article_list = []
    article_eng_list = []
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
    with open(article_eng_file, "r+") as eng_file:
        list_raw = list(eng_file)
        for list_word in list_raw:
            article_eng_list.append(list_word.rstrip())
    with open(incorrect_eng_answer_file, "r+") as incorrect_eng_file:
        incorrect_list_raw = list(incorrect_eng_file)
        for incorrect_list_word in incorrect_list_raw:
            article_eng_list.append(incorrect_list_word.rstrip())
    incorrect_eng_file.close()
    pick_the_word(article, article_list, article_eng_list, incorrect_answer_file, incorrect_eng_answer_file, language)

def pick_the_word(article, article_list, article_eng_list, incorrect_answer_file, incorrect_eng_answer_file, language):
    if language == 1:
        word = article_list[random.randint(0, len(article_list) - 1)]
        if article in ("der", "das", "die"):
            print(article + "", word)
        if article not in ("der", "das", "die"):
            print(word)
        translation = article_eng_list[article_list.index(word)]
        original_translation = translation
        answer = str(input("Englisch?: "))
    if language == 2:
        word = article_eng_list[random.randint(0, len(article_eng_list) - 1)]
        print(word)
        original_translation = article_list[article_eng_list.index(word)]
        if article in ("der", "das", "die"):
            translation = article + " " + article_list[article_eng_list.index(word)]
        if article not in ("der", "das", "die"):
            translation = article_list[article_eng_list.index(word)]
        answer = str(input("Deutsch?: "))
    if answer.lower() == translation.lower():
        print("Richtig!")
        check_incorrect_file(incorrect_answer_file, incorrect_eng_answer_file, word, translation, language, original_translation)
        correct_count()
    if answer.lower() == "verlassen" or answer.lower() == "v" or answer.lower() == "quit" or answer.lower() == "q" and word.lower != "verlassen":
        end_of_game()
        quit()
    if answer.lower() != translation.lower():
        print("Es tut mir leid! Das ist nicht richtig!")
        print("Die richtige Antwort war: ", translation)
        add_to_incorrect_file(incorrect_answer_file, incorrect_eng_answer_file, word, translation, language, original_translation)
        incorrect_count()
    n = 1

def check_incorrect_file(incorrect_answer_file, incorrect_eng_answer_file, word, translation, language, original_translation):
    incorrect_list = []
    incorrect_eng_list = []
    with open(incorrect_answer_file, "r+") as incorrect_file:
        incorrect_list_raw = list(incorrect_file)
        for incorrect_list_word in incorrect_list_raw:
            incorrect_list.append(incorrect_list_word.rstrip())
        incorrect_file.close()
    with open(incorrect_eng_answer_file, "r+") as incorrect_eng_file:
        incorrect_eng_list_raw = list(incorrect_eng_file)
        for incorrect_eng_list_word in incorrect_eng_list_raw:
            incorrect_eng_list.append(incorrect_eng_list_word.rstrip())
        incorrect_eng_file.close()
    if language == 1:
        word = word
        translation = translation
    if language == 2:
        original_word = word
        word = original_translation
        translation = original_word
    if word in incorrect_list and translation in incorrect_eng_list:
        incorrect_list.remove(word)
        os.remove(incorrect_answer_file)
        with open(incorrect_answer_file, 'w+') as incorrect_file:
            for item in incorrect_list:
                incorrect_file.write("%s\n" % item)
        incorrect_file.close()
        incorrect_eng_list.remove(translation)
        os.remove(incorrect_eng_answer_file)
        with open(incorrect_eng_answer_file, 'w+') as incorrect_eng_file:
            for item in incorrect_eng_list:
                incorrect_eng_file.write("%s\n" % item)
        incorrect_eng_file.close()

def add_to_incorrect_file(incorrect_answer_file, incorrect_eng_answer_file, word, translation, language, original_translation):
    if language == 1:
        word = word
        translation = translation
    if language == 2:
        original_word = word
        word = original_translation
        translation = original_word
    with open(incorrect_answer_file, "a+") as incorrect_file:
        incorrect_file.write(word + "\n")
    incorrect_file.close()
    with open(incorrect_eng_answer_file, "a+") as incorrect_eng_file:
        incorrect_eng_file.write(translation + "\n")
    incorrect_eng_file.close()

def correct_count():
    var = 3
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Translation/streak_trans.txt"
            print("Streak: ")
        if var == 2:
            count_file = "../Storage Files/Game Function/Translation/correct_trans.txt"
            print("Correct: ")
        if var == 1:
            count_file = "../Storage Files/Game Function/Translation/incorrect_trans.txt"
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
            count_file = "../Storage Files/Game Function/Translation/streak_trans.txt"
            print("Streak: ")
            count = 0
            os.remove(count_file)
            with open(count_file, "w+") as count_item:
                count_item.write(str(count))
            count_item.close()
            print(count)
        if var == 2:
            count_file = "../Storage Files/Game Function/Translation/correct_trans.txt"
            print("Correct: ")
            with open(count_file, "r+") as count_item:
                count_list = list(count_item)
            count_item.close()
            count = int(count_list[0])
            print(count)
        if var == 1:
            count_file = "../Storage Files/Game Function/Translation/incorrect_trans.txt"
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
    with open("../Storage Files/Game Function/Translation/highscore_trans.txt") as file:
        highscore_list = [int(x) for x in file.read().split()]
    file.close()
    os.remove("../Storage Files/Game Function/Translation/highscore_trans.txt")
    print("-----------------------------------")
    while var > 0:
        if var == 3:
            count_file = "../Storage Files/Game Function/Translation/streak_trans.txt"
            highscore = highscore_list[0]
        if var == 2:
            count_file = "../Storage Files/Game Function/Translation/correct_trans.txt"
            highscore = highscore_list[0]
        if var == 1:
            count_file = "../Storage Files/Game Function/Translation/incorrect_trans.txt"
            highscore = -1
        with open(count_file, "r+") as count_item:
            count_list = list(count_item)
        count_item.close()
        count = int(count_list[0])
        if count > highscore and highscore != -1:
            highscore_list.remove(highscore)
            highscore_list.append(count)
            if var == 3:
                time.sleep(1)
                print("Final Streak: ", count)
            if var == 2:
                time.sleep(1)
                print("Final Correct: ", count)
            print("New high score!")
            print("-----------------------------------")
        if highscore > count:
            highscore_list.remove(highscore)
            highscore_list.append(highscore)
            if var == 3:
                time.sleep(1)
                print("Final Streak: ", count)
            if var == 2:
                time.sleep(1)
                print("Final Correct: ", count)
            print("High score: ", highscore)
            print("-----------------------------------")
        if highscore == -1:
            time.sleep(1)
            print("Final Incorrect: ", count)
            print("-----------------------------------")

        var = var - 1
    with open("../Storage Files/Game Function/Translation/highscore_trans.txt", "a+") as file:
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





translation()
