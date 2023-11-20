nom_produit = "pull"
prix_unitaire = 60
quantite_en_stock = 100
quantite_produit_achete = int(input("Entrez la quantité que vous souhaitez acheter : "))
resultat = quantite_en_stock - quantite_produit_achete
prix_client = quantite_produit_achete * prix_unitaire
inflation = 10
somme_produit_inflation = (prix_unitaire * inflation) // 100 + prix_unitaire
prix_client_inflation = quantite_produit_achete * somme_produit_inflation

print("================")
print("Informations du Produit")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire   : {prix_unitaire}€")
print(f"Quantité en stock : {quantite_en_stock} unités")
print("================")
print(f"Cout total pour {quantite_produit_achete} pull est de {prix_client}€ ")
print(f"Il reste {resultat} pull en stock")
print(f"Avec une inflation de {inflation}% le pull coutera dorénavant {somme_produit_inflation}€")
print("================")
print(f"Le client payerait donc ses {quantite_produit_achete} pull {prix_client_inflation}€ au lieu de {prix_client}€ avant inflation")
print("================")
print("Informations du Produit après inflation et achat client")
print(f"Prix unitaire   : {somme_produit_inflation}€")
print(f"Quantité en stock : {resultat} unités")





