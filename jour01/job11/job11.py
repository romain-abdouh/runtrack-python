chaine_caractere = input("écrirez votre chaine de caractères : ")

nombre_de_e = chaine_caractere.count('e')

if 'e' in chaine_caractere:
    print(f"La chaîne contient le caractère 'e' et elle y apparait {nombre_de_e} fois") 
else:
    print("La chaîne ne contient pas le caractère 'e'.")

