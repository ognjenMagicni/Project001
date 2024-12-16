def calculate_price_per_sqm_per_day(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # Extract headers and data
    headers = lines[0].strip()
    data = lines[1:]
    
    # Iterate through rows to calculate price per sqm per day
    results = []
    for line in data:
        row = line.strip().split(',')
        try:
            # Extract values based on their positions
            price = float(row[1])
            square_metre = float(row[2])
            number_of_nights = float(row[4])
            
            # Avoid division by zero
            if square_metre > 0 and number_of_nights > 0:
                price_per_sqm_per_day = price / (square_metre*number_of_nights)
                results.append(price_per_sqm_per_day)
            else:
                results.append(None)  # Handle invalid or zero values
        except (ValueError, IndexError):
            results.append(None)  # Handle malformed rows or non-numeric values
    
    return results

# Usage
file_name = 'Ime.txt'
prices_per_sqm_per_day = calculate_price_per_sqm_per_day(file_name)
print(prices_per_sqm_per_day)
print("Price per square metre per day:", sum(prices_per_sqm_per_day)/len(prices_per_sqm_per_day))

print(sorted(prices_per_sqm_per_day))
