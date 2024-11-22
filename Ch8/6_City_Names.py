def city_country(city_name, city_origin):
    full_city = f"{city_name.title()} is in {city_origin.title()}."
    return full_city

print(city_country('doha', 'qatar'))

print(city_country('abu dhabi', 'united arab emirates'))

print(city_country('muscat', 'oman'))