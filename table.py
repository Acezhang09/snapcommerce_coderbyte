import pandas as pd

if __name__ == "__main__":
    data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'
    
    # Removes the last \n terminator from the data to avoid creating an unused row
    data = data[:len(data)-1]

    # To seperate TO_FROM into two different columns when table is constructed
    data = data.replace('_', ';')

    # Generate table
    data_table = pd.DataFrame([i.split(';') for i in data.split("\n")])

    # TASK 1: Altering the FlightCodes column
    last_value = 0
    for i, value in enumerate(data_table[2]):
        # Skip over column title
        if i == 0: 
            pass
        # Sets a temp variable to be added by 10 through every iteration
        elif i == 1:
            # Convert FlightCodes column to int
            value = int(float(value))
            last_value = value
            data_table[2][i] = value

        else:
            # Adds 10 based of previous column value
            value = last_value + 10
            last_value = value
            data_table[2][i] = value

    # TASK 2: Change the To and From columns to uppercase
    for i, value in enumerate(data_table[3]):
        data_table[3][i] = value.upper()
    for i, value in enumerate(data_table[4]):
        data_table[4][i] = value.upper()

    # TASK 3: Clean up Airline Code column
    for count, value in enumerate(data_table[0]):
        first_index = None
        last_index = None
        # Splits the string based on the index of the first and last alphabetical chars
        for i, c in enumerate(value):
            if c.isalpha():
                if first_index == None:
                    first_index = i
                else:
                    last_index = i
        data_table[0][count] = value[first_index:last_index+1]
    
    print(data_table)