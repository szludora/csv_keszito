import shutil


def csv_ir(csv):
    my_file_name = input("Fájl neve: ")

    f = open(f"{my_file_name}.csv", "w")
    f.write(csv)
    f.close()
    f = open(f"{my_file_name}.csv", "r")
    f.close()

    path_to_file = f'C:/Users/Dóra/OneDrive/Dokumentumok/Python/csv_keszito/dist/{my_file_name}.csv'
    path_to_folder = 'C:/Users/Dóra/OneDrive/Dokumentumok/Python/csv_keszito/naptárak'
    shutil.move(path_to_file, path_to_folder)
