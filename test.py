import pycountry

def detect_country(province):
    # Convert the province to title case for better matching
    province = province.title()
    
    # Iterate over all subdivisions and check if the province is in their names
    for subdivision in pycountry.subdivisions:
        if subdivision.name == province:
            country_code = subdivision.country_code
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                return country.name
    
    # If the province is not found in any subdivision, return None
    return None

# Example usage
province = "Provincia di Pisa"  # Example province
country = detect_country(province)
if country:
    print(f"The province {province} is in {country}.")
else:
    print(f"Unable to detect the country for the province {province}.")
