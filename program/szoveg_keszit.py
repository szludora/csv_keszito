def szoveget_keszit(honap, adat):

    csv = "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description"

    i = 0
    while i < len(adat):
        if adat[i] == "H":
            csv += f'' \
                   f'D,{honap}/{i + 1}/2023,5:00'\
                   f',{honap}/{i + 1}/2023,13:30 PM,' \
                    'FALSE,'

        elif adat[i] == "R":
            csv += f'D,{honap}/{i+1}/2023,6:00' \
                   f',{honap}/{i+1}/2023,14:30 PM,' \
                   f'FALSE,'

        elif adat[i] == "DE":
            csv += f'D,{honap}/{i + 1}/2023,9:00' \
                   f',{honap}/{i + 1}/2023,18:30 PM,' \
                   f'FALSE,'
        elif adat[i] == "DU":
            csv += f'D,{honap}/{i + 1}/2023,6:00' \
                   f',{honap}/{i + 1}/2023,14:30 PM,' \
                   f'FALSE,'

        elif adat[i] == "E":
            csv += f'D,{honap}/{i + 1}/2023,10:00 PM"' \
                   f',{honap}/{i + 2}/2023,6:30 AM,' \
                   f'FALSE,'
        elif adat[i] == "P":
            pass

        else:
            csv += ''
        i += 1

    return csv
