def city_country(city , country):
    cities = city.title() + ", " + country.title()
    return cities
city = city_country("santiago" , "chile")
print(city)