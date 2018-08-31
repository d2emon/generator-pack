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
    village_distance = ""
    if kingdom.villages.distance:
        village_distance = "The average distance between villages is {distance:.1f}km.\n".format(
            distance=kingdom.villages.distance
        )
    town_distance = ""
    if kingdom.towns.distance:
        town_distance = "The average distance between towns is {distance:.1f}km.\n".format(
            distance=kingdom.towns.distance
        )
    city_distance = ""
    if kingdom.cities.distance:
        city_distance = "The average distance between cities (including big cities) is {distance:.1f}km.\n".format(
            distance=kingdom.cities.distance
        )

    return (
        "{kingdom.name}'s population is approximately {kingdom.population} persons.\n"
        + "{kingdom.hermits.population} residents are isolated or itinerant.\n"
        + "{kingdom.villages.population} residents live in {kingdom.villages.settlements} villages.\n"
        + "{kingdom.towns.population} residents live in {kingdom.towns.settlements} towns.\n"
        + "{kingdom.cities.population} residents live in {kingdom.cities.settlements} cities.\n"
        + "{kingdom.big_cities.population} residents live in {kingdom.big_cities.settlements} big cities.\n"
        + "{village_distance}"
        + "{town_distance}"
        + "{city_distance}"
        + "{kingdom.name} supports {kingdom.universities} Universities.\n"
        + "{kingdom.name} supports {kingdom.livestock} head of livestock:\n"
        + "{kingdom.fowl} fowl (e.g. chickens, geese, ducks).\n"
        + "{kingdom.meat_animals} dairy and meat animals (e.g. cows, goats, pigs, sheep)."
    ).format(
        kingdom=kingdom,
        village_distance=village_distance,
        town_distance=town_distance,
        city_distance=city_distance,
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
        land_mass_description(kingdom, map_hex),
        population_description(kingdom),
        castles_description(kingdom),
    )
