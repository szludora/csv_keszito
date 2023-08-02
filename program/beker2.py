def bekerni1():
    honap = 0
    while honap < 1 or honap > 12:
        honap = int(input("hónap:\n"))
    return honap


def bekerni2():

    napok = input("Így dolgozom (r, ny, k, z, p):\n")
    lista = []
    """
    'de du e e'
    """
    i = 0
    while i < len(napok)-1:
        if napok[i] != " ":
            if napok[i+1] == " ":
                lista.append(napok[i].upper())
            else:
                napszak = f"{napok[i]+napok[i+1]}"
                lista.append(napszak.upper())
        i += 1
    if napok[i] != " " and napok[i-1] == " ":
        lista.append(napok[i].upper())
    print(lista)
    return lista
