# Using the URL - https://restcountries.com/v3.1/all write a python program which will do the following
# 1. Use the OOPS concept for the following task
# 2. Use the class constructor for taking input from the above URL for the task
# 3. Create a method that will fetch all the JSON data from the URL mentioned above
# 4. Create a method that will display the name of the countries, currencies and currency symbols
# 5. Create a method that will display all those countries which have Dollar as its currency
# 6. Create a method that will display all those countries which have Euro as its currency

import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        """Fetch all JSON data from the URL."""
        response = requests.get(self.url)
        response.raise_for_status()  # This will raise an error for bad responses
        return response.json()

    def display_country_currency_info(self):
        """Display the name of the countries, currencies, and currency symbols."""
        print("Country, Currency, and Symbol Information:")
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")
        print("\n")

    def display_countries_with_dollar(self):
        """Display all countries which have Dollar as its currency."""
        dollar_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                if 'Dollar' in currency_info.get('name', ''):
                    dollar_countries.append(country.get('name', {}).get('common', 'N/A'))
        print("Countries using Dollar as currency:")
        if dollar_countries:
            for country in dollar_countries:
                print(country)
        else:
            print("No countries use Dollar as currency.")
        print("\n")

    def display_countries_with_euro(self):
        """Display all countries which have Euro as its currency."""
        euro_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                if 'Euro' in currency_info.get('name', ''):
                    euro_countries.append(country.get('name', {}).get('common', 'N/A'))
        print("Countries using Euro as currency:")
        if euro_countries:
            for country in euro_countries:
                print(country)
        else:
            print("No countries use Euro as currency.")
        print("\n")

# URL for fetching the country data
url = "https://restcountries.com/v3.1/all"

# Create an instance of the CountryData class
country_data = CountryData(url)

# Display country, currency, and symbol information
country_data.display_country_currency_info()

# Display countries with Dollar as their currency
country_data.display_countries_with_dollar()

# Display countries with Euro as their currency
country_data.display_countries_with_euro()