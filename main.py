import pandas as pd



symbol_table = {}


def parsing_location_counter(location_counter):
    if(type(location_counter == "str")):
        location_counter = int(location_counter)
    elif(type(location_counter == "int")):
        location_counter = hex(location_counter)
    return location_counter
         


if __name__ == "__main__":
    table = pd.read_csv("table.csv")
    table["Address"] = "" #adding new column
    location_counter = table.at[0,"Reference"]
    starting_address= location_counter
    print(type(location_counter))

    for index,column in table.iterrows():
        label = column["Labels"]
        instructions = column["Instructions"]
        reference = column["Reference"]

        if(instructions == "Start"  or index == 1):

            table.at[index,"Address"] = starting_address
            symbol_table["label"] = location_counter
        elif(instructions == "RESB" or instructions == "RESW"):
            pass
        elif(instructions == "Byte"):
            if (reference.startswith("C'")):
                pass
            elif(reference.startswith("X'")):
                pass

        else:
            location_counter = parsing_location_counter(location_counter)
            location_counter +=3
            print(type(location_counter))
            table.at[index,"Address"] = location_counter 
    
    
    print(table)

                
        
          



    


