from program import dora
from program import bogi
from program import ujprogram


def naptart_ir():

    nev = 0
    while nev < 1 or nev > 3:
        nev = int(input("1. Dóra\n"
                        "2. Bogi\n"
                        "3. Új\n"))
    if nev == 1:
        dora.naptar()
    elif nev == 2:
        bogi.naptar()
    else:
        ujprogram.beker()
