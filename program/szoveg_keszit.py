def szoveget_keszit(honap, adat):

    csv = "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description\n"

    i = 0
    while i < len(adat):
        if adat[i] == "H":
            csv += f'D,{honap}/{i + 1}/2023,5:00'\
                   f',{honap}/{i + 1}/2023,13:30 PM,' \
                    'FALSE,\n'

        elif adat[i] == "R":
            csv += f'D,{honap}/{i+1}/2023,6:00' \
                   f',{honap}/{i+1}/2023,14:30 PM,' \
                   f'FALSE,\n'

        elif adat[i] == "DE":
            csv += f'D,{honap}/{i + 1}/2023,9:00' \
                   f',{honap}/{i + 1}/2023,18:30 PM,' \
                   f'FALSE,\n'
        elif adat[i] == "DU":
            csv += f'D,{honap}/{i + 1}/2023,6:00' \
                   f',{honap}/{i + 1}/2023,14:30 PM,' \
                   f'FALSE,\n'

        elif adat[i] == "E":
            csv += f'D,{honap}/{i + 1}/2023,10:00 PM' \
                   f',{honap}/{i + 2}/2023,6:30 AM,' \
                   f'FALSE,\n'
        elif adat[i] == "P":
            pass

        else:
            pass
        i += 1

    return csv
