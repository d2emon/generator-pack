"""
While the average distance between population centers can be derived from the total land area, the average walking
distance from one village to the next is more realistically determined by considering only the settled land. Villages
and towns tend to cluster tightly along the arteries of travel defined by the lines between the cities - leaving gaps
of wilderness in the middle.
"""
SETTLED_MILE_SUPPORT = 180


def settled(population):
    """
    A square mile of settled land (including requisite roads, villages and towns, as well as crops and pastureland)
    will support 180 people. This takes into account normal blights, rats, drought, and theft, all of which are common
    in most worlds. If magic is common, the GM may decide a square mile of land can support many more people. Note that
    the number of people a square mile of agricultural land will support is not the same as the maximum population
    density for a kingdom.

    :param population:
    :return:
    """
    return population / SETTLED_MILE_SUPPORT


def wilderness(area=1000, settled_area=500):
    """
    Once you've decided the ability of the land to support people, you can determine the amount of wilderness/
    unfarmable country in the kingdom by working backwards. Take the example kingdom of Chamlek again. With one
    square mile supporting 180 people, that means there are approximately 37,000 square miles of developed agrarian
    land - about 42% of the total area of the isle. This offers a graphic example of just how sparse the population
    really is. The remaining 58% of the country is wilderness, rivers and lakes.

    Even if Chamlek had the maximum population density (120 people per square mile), the farmland would be a whopping
    2/3rds of the total land, leaving one-third of the country to wilderness (mostly forested hills between the farms)
    and waterways. That's somewhere near the absolute maximum, given Earthly conditions, though higher is theoretically
    possible if the GM determines that the entire country is arable.

    :param area:
    :param settled_area:
    :return:
    """
    return area - settled_area
