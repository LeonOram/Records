class country:
    def __init__(self):
            self.name = '-'
            self.capital = '-'
            self.currency = '-'

# main program
country_list = []
for count in range(2):
    country = country()
    country.name = input("Name of country: ")
    country.capital = input("Capital city: ")
    country.currency = input("Currency used: ")
    country_list.append(country)
