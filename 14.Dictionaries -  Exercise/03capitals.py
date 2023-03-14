countries = input().split(', ')
capitals = input().split(', ')
country_capital_dict = {countries[i]:capitals[i] for i in range(len(countries))}
print("\n".join(f'{country} -> {capital}' for country, capital in country_capital_dict.items()))



