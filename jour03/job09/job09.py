def moyenne (note1, note2, note3):
    result = (note1 + note2 + note3) / 3
    return result


note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant <= 20 and moyenne_etudiant >= 15 :
    print(f"{moyenne_etudiant} : Très bon élève")
elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11 :
    print(f"{moyenne_etudiant} : Bon élève")
elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8 :
    print(f"{moyenne_etudiant} :Élève moyen")
else:
    print(f"{moyenne_etudiant} :Élève devant faire des efforts")