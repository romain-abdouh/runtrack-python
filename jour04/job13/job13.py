L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(L)

liste_sans_doublons = []

for element in L:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

print(f"Liste après la suppression des doublons :{liste_sans_doublons}")