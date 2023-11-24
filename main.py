import pandas as pd

symbol_table = {}


def pass1(table):
     
    
     location_counter = (table.at[0, "Reference"])
     starting_address = location_counter

     for index, column in table.iterrows():
        label = column["Labels"]
        instructions = column["Instructions"]
        reference = column["Reference"]

        if instructions == "Start" or index == 1:
            table.at[index, "Address"] = starting_address
        elif instructions == "RESB" or instructions == "RESW":

            table.at[index, "Address"] = f"{location_counter:04X}"

            take_reference = int(table.at[index,"Reference"])*3
            take_reference = hex(take_reference)
            print(take_reference)
            location_counter += int(f"{take_reference}",16)

        elif instructions == "Byte":
            if reference.startswith("C'"):
                pass
            elif reference.startswith("X'"):
                pass
        elif index == 2:
            location_counter = 0x1003  # Set the correct value directly in hex
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        else:
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        table['Labels'].fillna(';', inplace=True)
        return table

if __name__ == "__main__":
    table = pd.read_csv("table.csv")
    table["Address"] = ""  # adding a new column
    location_counter = (table.at[0, "Reference"])
    starting_address = location_counter

    for index, column in table.iterrows():
        label = column["Labels"]
        instructions = column["Instructions"]
        reference = column["Reference"]

        if instructions == "Start" or index == 1:
            table.at[index, "Address"] = starting_address
        elif instructions == "RESB" or instructions == "RESW":

            table.at[index, "Address"] = f"{location_counter:04X}"

            take_reference = int(table.at[index,"Reference"])*3
            take_reference = hex(take_reference)
            print(take_reference)
            location_counter += int(f"{take_reference}",16)

        elif instructions == "Byte":
            if reference.startswith("C'"):
                pass
            elif reference.startswith("X'"):
                pass
        elif index == 2:
            location_counter = 0x1003  # Set the correct value directly in hex
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        else:
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        table['Labels'].fillna(';', inplace=True)
    print(table)
