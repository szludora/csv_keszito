import shutil


def szoveget_keszit(nev, napok, kezdesek, vegzesek, honap, adat):
    csv = "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description\n"
    lista = []

    r = 0
    while r < len(adat):
        if adat[r] != " ":
            if r + 1 < len(adat) and adat[r + 1] != " ":
                napszak = f"{adat[r]}{adat[r + 1]}"
                lista.append(napszak.upper())
                r += 1
            else:
                lista.append(adat[r].upper())
        r += 1

    print(lista)

    i = 0
    while i < len(lista):
        x = 0
        while x < len(napok):
            if lista[i].upper() == napok[x].upper():   # print(repr(lista[i]), repr(napok[x]))
                csv += f'{nev},{honap}/{i + 1}/2023,{kezdesek[x]}:00,' \
                       f'{honap}/{i + 1}/2023,{vegzesek[x]}:00,' \
                       'FALSE,\n'
            x += 1

        i += 1

    return csv


def csv_ir(csv):
    my_file_name = input("Fájl neve: ")

    f = open(f"{my_file_name}.csv", "w")
    f.write(csv)
    f.close()
    f = open(f"{my_file_name}.csv", "r")
    f.close()

    path_to_file = f'C:/Users/Dóra/OneDrive/Dokumentumok/Python/csv_keszito/{my_file_name}.csv'
    path_to_folder = 'C:/Users/Dóra/OneDrive/Dokumentumok/Python/csv_keszito/naptárak'
    shutil.move(path_to_file, path_to_folder)


def beker():
    nev = input("Név: \n")
    nap = input("Múszakok: ")
    kezdes = input("Kezdetük: pl 8, 12, 15, 16 ")
    meddig = int(input("Mennyi idő a műszakod? pl.: 8"))
    honap = int(input("melyik hónap?"))
    adat = input("így dolgozom: ").upper()

    napok = nap.split(",")
    napok = [nap.strip() for nap in napok]

    kezdesek = kezdes.split(",")
    vegzesek = []
    print(kezdesek)
    i = 0
    while i < len(kezdesek):
        vegzesek.append(int(kezdesek[i]) + meddig)
        i += 1

    csv = szoveget_keszit(nev, napok, kezdesek, vegzesek, honap, adat)
    csv_ir(csv)
