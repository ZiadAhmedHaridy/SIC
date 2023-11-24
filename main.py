import pandas as pd


object_code = []  # List to store object code
symbol_table = {}

OPTAB = {
    "FIX": ["1", "C4"],
    "FLOAT": ["1", "C0"],
    "HIO": ["1", "F4"],
    "NORM": ["1", "C8"],
    "SIO": ["1", "F0"],
    "TIO": ["1", "F8"],
    "ADDR": ["2", "90"],
    "CLEAR": ["2", "B4"],
    "COMPR": ["2", "A0"],
    "DIVR": ["2", "9C"],
    "MULR": ["2", "98"],
    "RMO": ["2", "AC"],
    "SHIFTL": ["2", "A4"],
    "SHIFTR": ["2", "A8"],
    "SUBR": ["2", "94"],
    "SVC": ["2", "B0"],
    "TIXR": ["2", "B8"],
    "ADD": ["3", "18"],
    "ADDF": ["3", "58"],
    "AND": ["3", "40"],
    "COMP": ["3", "28"],
    "COMPF": ["3", "88"],
    "DIV": ["3", "24"],
    "DIVF": ["3", "64"],
    "J": ["3", "3C"],
    "JEQ": ["3", "30"],
    "JGT": ["3", "34"],
    "JLT": ["3", "38"],
    "JSUB": ["3", "48"],
    "LDA": ["3", "00"],
    "LDB": ["3", "68"],
    "LDCH": ["3", "50"],
    "LDF": ["3", "70"],
    "LDL": ["3", "08"],
    "LDS": ["3", "6C"],
    "LDT": ["3", "74"],
    "LDX": ["3", "04"],
    "LPS": ["3", "D0"],
    "MUL": ["3", "20"],
    "MULF": ["3", "60"],
    "OR": ["3", "44"],
    "RD": ["3", "D8"],
    "RSUB": ["3", "4C"],
    "SSK": ["3", "EC"],
    "STA": ["3", "0C"],
    "STB": ["3", "78"],
    "STCH": ["3", "54"],
    "STF": ["3", "80"],
    "STI": ["3", "D4"],
    "STL": ["3", "14"],
    "STS": ["3", "7C"],
    "STSW": ["3", "E8"],
    "STT": ["3", "84"],
    "STX": ["3", "10"],
    "SUB": ["3", "1C"],
    "SUBF": ["3", "5C"],
    "TD": ["3", "E0"],
    "TIX": ["3", "2C"],
    "WD": ["3", "DC"]
}

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
        elif  instructions == "RESW":

            table.at[index, "Address"] = f"{location_counter:04X}"

            take_reference = int(table.at[index,"Reference"])*3
            take_reference = hex(take_reference)
            location_counter += int(f"{take_reference}",16)

        elif instructions == "RESB" :
            table.at[index, "Address"] = f"{location_counter:04X}"
            take_reference = int(table.at[index,"Reference"])
            take_reference = hex(take_reference)
            location_counter += int(f"{take_reference}",16)

        elif instructions == "Byte":
              if reference.startswith("C'"):
                    object_code.append(reference[2:-1])  # Extract characters
              elif reference.startswith("X'"):
                object_code.append(reference[2:-1])  # Extract hex values
        elif index == 2:
            location_counter = 0x1003  # Set the correct value directly in hex
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        else:
            table.at[index, "Address"] = f"{location_counter:04X}"
            location_counter += 3
        if label != ';':
            symbol_table[label] = f"{int(location_counter):04X}"
        table["Labels"].fillna(';', inplace=True)
        end_address = table.iloc[-1]['Address']
        length_of_program = end_address
   
    for index, column in table.iterrows():
        label = column["Labels"]
        instructions = column["Instructions"]
        reference = column["Reference"] 
        address = column["Address"]
        if(instructions == "Start"):
            continue
        elif(instructions in OPTAB):
            x = "0"
            hex_values = []
            opcode = OPTAB[instructions][1]
            print(opcode , address)
            opcode_binary = bin(int(opcode, 16))[2:].zfill(8)
            address_binary = x+bin(int(address, 16))[2:].zfill(15)
            
            combined_binary = opcode_binary  + address_binary
            print(opcode_binary,x,address_binary)
            for i in range(0, len(combined_binary), 4):
                four_bits = combined_binary[i:i + 4]
                hex_value = hex(int(four_bits, 2))[2:]  # Convert 4 bits to hex
                hex_values.append(hex_value)
            print(hex_values)
            
    print(table)
    print(symbol_table)
    print("length of programmer -> "+length_of_program)

