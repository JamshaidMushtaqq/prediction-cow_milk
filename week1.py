# TASK 1 - Record the yield
def record_yield():
    data = {}
    for i in range(7):  # Loop for each day of the week
        for i in range(2):  # Loop for each milking session
            while True:
                cow_id = input("Enter cow ID (3-digit code): ")
                if len(cow_id) == 3 and cow_id.isdigit():
                    break
                print("Invalid cow ID. Please enter a 3-digit numeric code.")

            while True:
                try:
                    yield_value = float(input("Enter yield in litres: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for yield.")

            data.setdefault(cow_id, []).append(yield_value)
    return data


# TASK 2 - Calculate the statistics
def calculate_statistics(data):
    total_volume = sum(sum(yields) for yields in data.values())
    total_cows = len(data)

    average_yield = total_volume // total_cows

    print("Total weekly volume of milk:", round(total_volume))
    print("Average yield per cow in a week:", round(average_yield))


# TASK 3 - Identify the most productive cow and cows with low volume
def identify_cows(data):
    most_productive_cow = max(data, key=lambda x: sum(data[x]))
    low_volume_cows = [cow_id for cow_id, yields in data.items() if len([yield_value for yield_value in yields if yield_value < 12]) >= 4]
    
    print("Most productive cow ID:", most_productive_cow)
    print("Weekly yield of the most productive cow:", sum(data[most_productive_cow]))
    
    print("Cows with low volume (less than 12 liters on 4 or more days):",low_volume_cows)
    for cow_id in low_volume_cows:
        print("Cow ID:", cow_id)
        print("Weekly yield:", sum(data[cow_id]))
    
    return most_productive_cow, low_volume_cows

# main program
yield_data = record_yield()
calculate_statistics(yield_data)
identify_cows(yield_data)
