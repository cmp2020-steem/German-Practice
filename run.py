answer = input("(1) Wörter hinzufügen,(2) Geschlecht erraten, oder (3) Wortübersetzung?: ")
if answer == "Wörter hinzufügen" or answer == "1":
    import Add_Term
if answer == "Geschlecht erraten" or answer == "2":
    import Gender_Guess
if answer == "Wortübersetzung" or "3":
    import Translation