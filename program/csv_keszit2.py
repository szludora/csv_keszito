def csv_ir(csv):
    f = open(f"bogi_naptar.csv", "w")
    f.write(csv)
    f.close()
    f = open("bogi_naptar.csv", "r")
    f.close()
