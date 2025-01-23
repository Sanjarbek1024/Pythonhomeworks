from bs4 import BeautifulSoup

# First step: Parsing the HTML using BeautifulSoup
soup = BeautifulSoup(open('weather.html'), 'html.parser')

# Second step: Extracting the table rows
table_rows = soup.find('table').find('tbody').find_all('tr')

# Third step: Initializing variables for processing
weather_data = []
highest_temp = float('-inf')
highest_temp_day = ""
sunny_days = []
total_temp = 0

# Step 4: Processing each row
for row in table_rows:
    columns = row.find_all('td')
    day = columns[0].text.strip()
    temperature = int(columns[1].text.strip().replace('°C', ''))
    condition = columns[2].text.strip()
    
    # Step 5: Adding data to weather_data list
    weather_data.append({"day": day, "temperature": temperature, "condition": condition})
    
    # Step 6: Checking for the highest temperature
    if temperature > highest_temp:
        highest_temp = temperature
        highest_temp_day = day
    
    # Step 7: Checking for sunny days
    if condition.lower() == "sunny":
        sunny_days.append(day)
    
    # Step 8: Finding the total temperatures for average calculation
    total_temp += temperature

# Step 8: Calculating the average temperature
average_temp = total_temp / len(weather_data)

# Showing the final results
print("Weather Data:")
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}")

print(f"\nDay with the highest temperature: {highest_temp_day} ({highest_temp}°C)")
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")
print(f"Average temperature for the week: {average_temp:.2f}°C")

