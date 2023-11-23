def verifier(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            print (f"{nombre} est un nombre entier, positif et pair.")
        else:
            print (f"{nombre} est un nombre entier, positif et impair.")
    else:
        print (f"{nombre} n'est pas un nombre entier et positif.")


verifier(10)
verifier(7)
verifier(3.5)
verifier(0)
verifier(-4)

