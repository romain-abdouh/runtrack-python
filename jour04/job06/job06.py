def liste_nombre ():
    list = [1, 2, 3, 4, 5]
    print(list)

    list[0], list[-1] = list[-1], list[0]
    print(list)



liste_nombre()