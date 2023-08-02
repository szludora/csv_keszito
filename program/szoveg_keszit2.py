def szoveget_keszit(honap, adat):

    csv = "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description"

    i = 0
    while i < len(adat):
        if adat[i] == "R":
            csv += f"B,{honap}/{i + 1}/2023,8:00"\
                   f",{honap}/{i + 1}/2023,5:00 PM," \
                    "FALSE,"

        elif adat[i] == "NY":
            csv += f'B,{honap}/{i+1}/2023,10:00' \
                   f',{honap}/{i+1}/2023,7:00 PM,' \
                   f'FALSE,'

        elif adat[i] == "K":
            csv += f'B,{honap}/{i + 1}/2023,11:00' \
                   f',{honap}/{i + 1}/2023,8:00 PM,"' \
                   f'FALSE,'
        elif adat[i] == "Z":
            csv += f'B,{honap}/{i + 1}/2023,12:30' \
                   f',{honap}/{i + 1}/2023,9:30 PM,' \
                   f'FALSE,'

        elif adat[i] == "VN":
            csv += f'B,{honap}/{i + 1}/2023,9:00' \
                   f',{honap}/{i + 1}/2023,6:00 PM,' \
                   f'FALSE,'
        elif adat[i] == "VZ":
            csv += f'B,{honap}/{i + 1}/2023,9:30' \
                   f',{honap}/{i + 1}/2023,6:30 PM,' \
                   f'FALSE,'
        elif adat[i] == "P":
            pass
        else:
            csv += ""
        i += 1

    return csv
