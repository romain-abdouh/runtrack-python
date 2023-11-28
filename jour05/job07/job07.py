def arrondir_notes(notes):
    resultats = []
    for note in notes:
        if note < 40:
            resultats.append(note)
        else:
            multiple_de_5_superieur = (note // 5 + 1) * 5
            note_arrondie = multiple_de_5_superieur 
            if multiple_de_5_superieur - note < 3:
                resultats.append(note_arrondie)
            else:
                resultats.append(note)
    return resultats

notes_etudiants = [83, 38, 41, 55, 68, 12]
notes_arrondies = arrondir_notes(notes_etudiants)

print(f"Notes originales : {notes_etudiants}")
print(f"Notes arrondies : {notes_arrondies}")

for i, note_arrondie in enumerate(notes_arrondies):
    if note_arrondie < 40:
        print(f"{note_arrondie} est trop bas, tu as échoué")
    else:
        print(f"{note_arrondie} tu as réussi")
