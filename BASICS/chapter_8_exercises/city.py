#Exercises

def city_country(country, city):

    """" This Function Returns a String of Country and City """

    full_country_name = f"The Country is '{country}' and the City is '{city}'"
    return full_country_name.title()

first_country = city_country('Cameroon', 'Douala')
print(first_country)

second_country = city_country('Nigeria', 'Lagos')
print(second_country)

third_country = city_country('USA', 'california')
print(third_country)