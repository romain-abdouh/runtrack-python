table = int(input("Veuillez saisir un entier supérieur à zéro : "))

if table > 0:    
    for nombre in range(1, table + 1):
        print(f"Table de multiplication de {nombre} :")
        for j in range(1, 11):
            produit = nombre * j
            print(f"{nombre} x {j} = {produit}")  
else:
    print("entrez un entier supérieur à 0")