from program import dora
from program import bogi


def naptart_ir():
    nev = 0
    while nev < 1 or nev > 2:
        nev = int(input("1. Dóra\n"
                        "2. Bogi\n"))
    if nev == 1:
        dora.naptar()
    else:
        bogi.naptar()
