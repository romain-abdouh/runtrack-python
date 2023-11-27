def tri_insertion(arr):
    for i in range(1, 1000):
        if arr[i] is None:
            break
        cle = arr[i]
        j = i - 1
        while j >= 0 and cle < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle

def arrondir_et_trier(liste):
    for i in range(1000): 
        if liste[i] is None:
            break
        partie_entiere = liste[i] // 1
        decimal = liste[i] - partie_entiere
        if decimal >= 0.5:
            liste[i] = partie_entiere + 1
        else:
            liste[i] = partie_entiere

    tri_insertion(liste)

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50, None] 


arrondir_et_trier(ma_liste)
ma_liste.pop()

print("Liste arrondie et triée :", ma_liste)