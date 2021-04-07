def add_term(article, string_list):
    article = string_list[0]
    if article in ("der", "das", "die", "v", "verb", "adj", "adjektiv", "adv", "adverb", "präposition", "prep"):
        if len(string_list) == 1:
            germ_term = input("Deutsch?: ")
            eng_term = input("Englisch?: ")
        if len(string_list) == 2:
            germ_term = string_list[1]
            eng_term = input("Englisch?: ")
        if len(string_list) == 3:
            germ_term = string_list[1]
            eng_term = string_list[2]
        if len(string_list) > 3:
            germ_term = string_list[1]
            eng_term = string_list[2]
            index = 3
            while index < len(string_list):
                eng_term = eng_term + " " + string_list[index]
                index = index + 1
    if article in ("phrase", "ph"):
        germ_term = str(input("Deutsch?: "))
        eng_term = str(input("Englisch?:"))
    finding_gender(article, germ_term, eng_term)
def finding_gender(article, germ_term, eng_term):
    if article.lower() == "der":
        article_file = "../Storage Files/Words/der.txt"
        eng_article_file = "../Storage Files/Words/der_eng.txt"
    if article.lower() == "das":
        article_file = "../Storage Files/Words/das.txt"
        eng_article_file = "../Storage Files/Words/das_eng.txt"
    if article.lower() == "die":
        article_file = "../Storage Files/Words/die.txt"
        eng_article_file = "../Storage Files/Words/die_eng.txt"
    if article.lower() in ("verb", "v"):
        article_file = "../Storage Files/Words/verb.txt"
        eng_article_file = "../Storage Files/Words/verb_eng.txt"
    if article.lower() in ("adjektiv", "adj"):
        article_file = "../Storage Files/Words/adj.txt"
        eng_article_file = "../Storage Files/Words/adj_eng.txt"
    if article.lower() in ("adverb", "adv"):
        article_file = "../Storage Files/Words/adv.txt"
        eng_article_file = "../Storage Files/Words/adv_eng.txt"
    if article.lower() in ("phrase", "ph"):
        article_file = "../Storage Files/Words/phrases.txt"
        eng_article_file = "../Storage Files/Words/phrases_eng.txt"
    if article.lower() in ("Präposition", "prep"):
        article_file = "../Storage Files/Words/prep.txt"
        eng_article_file = "../Storage Files/Words/prep_eng.txt"
    text_scanner(germ_term, eng_term, article_file, eng_article_file)

def text_scanner(germ_term, eng_term, article_file, eng_article_file):
    germ_list = []
    eng_list = []
    with open(article_file, "r+") as file:
        germ_raw = list(file)
        for word in germ_raw:
            germ_list.append(word.rstrip())
    file.close()
    with open(eng_article_file, "r+") as file:
        eng_raw = list(file)
        for word in eng_raw:
            eng_list.append(word.rstrip())
    file.close()
    if germ_term in germ_list or eng_term in eng_list:
        print("Dieses Wort wurde bereits hinzugefügt!")
    if germ_term not in germ_list and eng_term not in eng_list:
        with open(article_file, "a+") as file:
            file.write(germ_term + "\n")
        file.close()
        with open(eng_article_file, "a+") as file:
            file.write(eng_term + "\n")
        file.close()
        print("Deutsch und Englisch hinzugefügt!")

x = 1
while x == 1:
    article = str(input("der, das, die, Verb, Adjektiv, Adverb, Präposition, oder Phrase?: "))
    string_list = article.split()
    if string_list[0].lower() in ("der", "das", "die", "verb", "v", "adjektiv", "adj", "adverb", "adv", "phrase", "ph", "präposition", "prep"):
        add_term(article, string_list)
        x = 1
    if string_list[0].lower() not in ("der", "das", "die", "verb", "v", "adjektiv", "adj", "adverb", "adv", "phrase", "ph", "präposition", "prep"):
        print("Beendet!")
        x = 0
        quit()
