# Using the URL https://www.openbrewerydb.org/documentation/ write a python script which will do the following
# 1. List the name of all breweries present in the states of Alaska, Maine and New York
# 2. What is the count of breweries in each of the states mentioned above
# 3. Count the number of types of breweries present in the individual cities of the state mentioned above
# 4. Count and list how many breweries have websites in the states of Alaska, Maine and New York


import requests

class BreweryData:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.states = ["Alaska", "Maine", "New York"]
        self.data = {state: self.fetch_data(state) for state in self.states}

    def fetch_data(self, state):
        """Fetch all JSON data for a given state."""
        response = requests.get(f"{self.base_url}?by_state={state}&per_page=100")
        response.raise_for_status()  # This will raise an error for bad responses
        return response.json()

    def list_breweries(self):
        """List the names of all breweries in the specified states."""
        for state, breweries in self.data.items():
            print(f"Breweries in {state}:")
            for brewery in breweries:
                print(brewery['name'])
            print("\n")

    def count_breweries(self):
        """Count the number of breweries in each of the specified states."""
        for state, breweries in self.data.items():
            print(f"Number of breweries in {state}: {len(breweries)}")

    def count_brewery_types_by_city(self):
        """Count the number of types of breweries in individual cities within the specified states."""
        for state, breweries in self.data.items():
            city_brewery_types = {}
            for brewery in breweries:
                city = brewery['city']
                brewery_type = brewery['brewery_type']
                if city not in city_brewery_types:
                    city_brewery_types[city] = {}
                if brewery_type not in city_brewery_types[city]:
                    city_brewery_types[city][brewery_type] = 0
                city_brewery_types[city][brewery_type] += 1
            
            print(f"Brewery types by city in {state}:")
            for city, types in city_brewery_types.items():
                print(f"{city}: {types}")
            print("\n")

    def count_breweries_with_websites(self):
        """Count and list how many breweries have websites in the specified states."""
        for state, breweries in self.data.items():
            breweries_with_websites = [brewery['name'] for brewery in breweries if brewery['website_url']]
            print(f"Breweries with websites in {state}: {len(breweries_with_websites)}")
            for brewery in breweries_with_websites:
                print(brewery)
            print("\n")

# Create an instance of the BreweryData class
brewery_data = BreweryData()

# List the names of all breweries in Alaska, Maine, and New York
brewery_data.list_breweries()

# Count the number of breweries in each of the states
brewery_data.count_breweries()

# Count the number of types of breweries in individual cities of each state
brewery_data.count_brewery_types_by_city()

# Count and list how many breweries have websites in the states
brewery_data.count_breweries_with_websites()