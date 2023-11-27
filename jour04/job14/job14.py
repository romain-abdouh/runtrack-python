def my_long_word(longueur_minimale, phrase):
    mots = []
    mot_actuel = ""
    resultat = ""

    for caractere in phrase:
        if caractere.isalpha():
            mot_actuel += caractere
        elif mot_actuel != "":
            longueur_mot = 0
            for _ in mot_actuel:
                longueur_mot += 1

            if longueur_mot > longueur_minimale:
                if resultat:
                    resultat += " "
                resultat += mot_actuel
            mot_actuel = ""

    if mot_actuel != "":
        longueur_mot = 0
        for _ in mot_actuel:
            longueur_mot += 1

        if longueur_mot > longueur_minimale:
            if resultat:
                resultat += " "
            resultat += mot_actuel

    return resultat

longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(phrase)

resultat = my_long_word(longueur_minimale, phrase)
print(f"avec des mots de plus de 4 lettres : {resultat}")