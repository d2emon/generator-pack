from .density import descriptions as development_descriptions


def land_mass_description(kingdom, map_hex=None):
    hex_text = ""
    if map_hex:
        hex_text = " ({})".format(map_hex.describe(kingdom.area))

    density = "{} persons per km² ({})".format(
        kingdom.density,
        development_descriptions.get(kingdom.development)
    )

    return (
        "The population density of {kingdom.name}, due to factors such as climate, geography, and political "
        + "environment, is {density}.\n"
        + "{kingdom.name} occupies {kingdom.area}km²{hex}. Roughly {kingdom.arable_percent}% of this is arable land, "
        + "or {kingdom.arable}km². The remaining {kingdom.wilderness}km² is divided among wilderness, rivers, "
        + "lakes, and the like."
    ).format(
        kingdom=kingdom,
        hex=hex_text,
        density=density,
    )


def population_description(kingdom):
    return (
        "{kingdom.name}'s population is approximately {kingdom.population} persons.\n"
        + "{kingdom.hermits} residents are isolated or itinerant.\n"
        + "{kingdom.village_population} residents live in {kingdom.villages} villages.\n"
        + "{kingdom.town_population} residents live in {kingdom.towns} towns.\n"
        + "{kingdom.city_population} residents live in {kingdom.cities} cities.\n"
        + "{kingdom.big_city_population} residents live in {kingdom.big_cities} big cities.\n"
        + "The average distance between villages is {kingdom.village_distance}km.\n"
        + "The average distance between towns is {kingdom.town_distance}km.\n"
        + "The average distance between cities (including big cities) is {kingdom.city_distance}km.\n"
        + "{kingdom.name} supports {kingdom.universities} Universities.\n"
        + "{kingdom.name} supports {kingdom.livestock} head of livestock:\n"
        + "{kingdom.fowl} fowl (e.g. chickens, geese, ducks).\n"
        + "{kingdom.meat_animals} dairy and meat animals (e.g. cows, goats, pigs, sheep)."
    ).format(
        kingdom=kingdom,
    )


def castles_description(kingdom):
    return (
        "The inhabitants of {kingdom.name} have been building castles for the last {kingdom.age} years.\n"
        + "There are approximately {kingdom.castles} standing fortifications in {kingdom.name}.\n"
        + "{kingdom.castles_active} castles are in active use.\n"
        + "{kingdom.ruins} castles are ruined or abandoned.\n"
        + "{kingdom.castles_civilized} castles are located in settled areas.\n"
        + "{kingdom.castles_wilderness} castles are located in remote areas, unsettled areas, or wilderness.\n"
        + "(All numbers are approximate, particularly where ruins and wilderness are concerned.)"
    ).format(
        kingdom=kingdom,
    )


def describe(kingdom, map_hex=None):
    return (
        "Land Mass\n{}\n\n"
        + "Population\n{}\n\n"
        + "Castles and Fortifications\n{}\n"
    ).format(
        land_mass_description(),
        population_description(),
        castles_description(),
    )
