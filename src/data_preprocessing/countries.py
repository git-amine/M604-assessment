import pycountry
import pycountry_convert as pc

country_error_handler={
"Yemen, Rep." : "Asia",
"West Bank and Gaza" : "Asia",
"Virgin Islands (U.S.)" : "North America",
"Venezuela, RB": "South America",
"Turkiye": "Asia",
"Timor-Leste":"Asia",
"St. Vincent and the Grenadines":"North America",
"St. Martin (French part)":"North America",
"Sint Maarten (Dutch part)":"North America",
"Micronesia, Fed. Sts.":"Oceania",
"Macao SAR, China":"Asia",
"Lao PDR":"Asia",
"Kosovo":"Europe",
"Korea, Rep." : "Asia",
"Korea, Dem. People's Rep." : "Asia",
"Iran, Islamic Rep." : "Asia",
"Hong Kong SAR, China" : "Asia",
"Gambia, The" : "Africa",
"Egypt, Arab Rep." : "Africa",
"Curacao" : "South America",
"Cote d'Ivoire" : "Africa",
"Congo, Rep." : "Africa",
"Congo, Dem. Rep." : "Africa",
"Channel Islands" : "Europe",
"Bahamas, The" : "North America"}


def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)

        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)

        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)

        return country_continent_name

    except Exception as e:
        if country_name in country_error_handler.keys():
            return country_error_handler.get(country_name)
        else:
         return f"Error : {str(e)}"





