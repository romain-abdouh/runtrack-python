montant_initial_investissement = 10000
taux_rendement_annuel = 10
gain_annuel_un_an = (montant_initial_investissement * taux_rendement_annuel) / 100
nouveau_capital_premiere_annee = montant_initial_investissement + gain_annuel_un_an
nouveau_capital = 5000 + nouveau_capital_premiere_annee
nouveau_taux_rendement = taux_rendement_annuel + 2
gain_annuel_deux_ans = (nouveau_capital * nouveau_taux_rendement) / 100
nouveau_capital_apres_gain_deux_ans = nouveau_capital + gain_annuel_deux_ans
retrait = (nouveau_capital_apres_gain_deux_ans * 10) / 100
diminution_rendement = nouveau_taux_rendement - 1 
nouveau_capital_apres_retrait = nouveau_capital_apres_gain_deux_ans - retrait
nouveau_gain_annuel_après_diminution_rendement = (nouveau_capital_apres_retrait * diminution_rendement) / 100
nouveau_capital_apres_trois_ans = nouveau_capital_apres_retrait + nouveau_gain_annuel_après_diminution_rendement

print(f"Avec un montant initial de {montant_initial_investissement} € et un taux de rendement annuel de {taux_rendement_annuel}%, le gain annuel sera de {gain_annuel_un_an}€ ")
print("==============")
print(f"En augmentant son capital de 5000€, soit {nouveau_capital}€, (ancien capital {montant_initial_investissement}€) et le taux de rendement de 2%, soit {nouveau_taux_rendement}%, (ancien taux {taux_rendement_annuel}), le nouveau gain de l'investiseur sera de {gain_annuel_deux_ans}€")
print("==============")
print(f"retrait de 10% du montant total, soit un retrait de {retrait}€")
print("==============")
print(f"le montant après retrait est de {nouveau_capital_apres_retrait}€")
print(f"Le nouveau gain final de l’investissement est de {nouveau_gain_annuel_après_diminution_rendement}€")
print(f"le montant final de l'investissement est de {nouveau_capital_apres_trois_ans}€")