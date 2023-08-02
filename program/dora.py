from program import beker as b
from program import szoveg_keszit as sz
from program import csv_keszit as cs


def naptar():

    honap = b.bekerni1()
    napok = b.bekerni2()
    csv = sz.szoveget_keszit(honap, napok)
    cs.csv_ir(csv)
