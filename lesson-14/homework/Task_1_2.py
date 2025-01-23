from bs4 import BeautifulSoup

# Parse the HTML using BeautifulSoup
def parse_weather(html):
    soup = BeautifulSoup(open("weather.html"), 'html.parser')
    rows = soup.find('table').find('tbody').find_all('tr')
    weather = []
    for row in rows:
        cols = row.find_all('td')
        weather.append({
            'day': cols[0].text.strip(),
            'temperature': int(cols[1].text.strip().replace('°C', '')),
            'condition': cols[2].text.strip()
        })
    return weather

# Find the day with the highest temperature
def find_hottest_day(weather):
    return max(weather, key=lambda x: x['temperature'])

# Find all days with specific condition
def find_days_by_condition(weather, condition):
    return [entry['day'] for entry in weather if entry['condition'].lower() == condition.lower()]

# Calculate the average temperature
def calculate_average_temperature(weather):
    total_temp = sum(entry['temperature'] for entry in weather)
    return total_temp / len(weather)

# Main processing
weather_data = parse_weather(open("weather.html"))
hottest_day = find_hottest_day(weather_data)
sunny_days = find_days_by_condition(weather_data, 'Sunny')
average_temp = calculate_average_temperature(weather_data)

# Display results
print("Weather Data:")
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}")

print(f"\nDay with the highest temperature: {hottest_day['day']} ({hottest_day['temperature']}°C)")
print(f"Day(s) with 'Sunny' condition: {', '.join(sunny_days)}")
print(f"Average temperature for the week: {average_temp:.2f}°C")
