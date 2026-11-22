# Q2. Long city names
# Print only the cities with more than 6 letters.
# Expected: Karachi, Peshawar, Bahawalpur

cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]
for city in cities :
    if len(city)>6:
        print(city)

