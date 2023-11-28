def distance_gardien(nbr_marches, hauteur_marche): 
    wc = (5 * nbr_marches) * 2
    distance = hauteur_marche * wc
    metre = distance // 100

    print(f"Pour {wc * 7} marches de {hauteur_marche}cm, le gardien parcourt {metre * 7}m par semaine.")
    

distance_gardien(30, 10)