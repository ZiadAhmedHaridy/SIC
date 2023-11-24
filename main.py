import pandas as pd



symbol_table = {}


def parsing_location_counter(location_counter):
    if type(location_counter) == str:
        location_counter = int(location_counter)
   
    return location_counter



if _name_ == "_main_":
    table = pd.read_csv("table.csv")
    table["Address"] = "" #adding new column
    location_counter = table.at[0,"Reference"]
    starting_address= location_counter

    for index,column in table.iterrows():
        label = column["Labels"]
        instructions = column["Instructions"]
        reference = column["Reference"]
        if(instructions == "Start"  or index == 1):

            table.at[index,"Address"] = starting_address
            symbol_table["label"] = location_counter
        elif(instructions == "RESB" or instructions == "RESW"):
            location_counter = parsing_location_counter(location_counter)
            
            table.at[index,"Address"] = location_counter 
            
            location_counter += int(reference)*3

        elif(instructions == "Byte"):
            if (reference.startswith("C'")):
                pass
            elif(reference.startswith("X'")):
                pass

        elif(index == 2):
            location_counter = parsing_location_counter(location_counter)
            location_counter  = 1003
            table.at[index,"Address"] = location_counter 
            location_counter +=3

        else:
              location_counter = parsing_location_counter(location_counter)
              table.at[index,"Address"] = location_counter 
              location_counter +=3


    
    
    print(table)