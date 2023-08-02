from program import beker2 as b
from program import szoveg_keszit2 as sz
from program import csv_keszit2 as cs


def naptar():
    honap = b.bekerni1()
    napok = b.bekerni2()
    csv = sz.szoveget_keszit(honap, napok)
    cs.csv_ir(csv)
