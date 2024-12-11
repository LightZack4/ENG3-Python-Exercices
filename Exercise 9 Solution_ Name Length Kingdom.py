city_data = []
while True:
    city_name = input("Please enter a city name (type 'stop' to end): ")

    if city_name.lower() == "stop":
        break

   
    population = len(city_name) * 1000000

   
    city_data.append({"name": city_name, "population": population})


sorted_city_data = sorted(city_data, key=lambda x: x["population"], reverse=True)


print("\nCities sorted by population (largest to smallest):")
for city in sorted_city_data:
    print(f"{city['name']} - Population: {city['population']}")
