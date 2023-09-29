"""
And now, the fun begins!

How to add a new Thing :

*   **name** is the referral name for this Thing. Unless a name generator is specified, this name will be the default name for any
    instances of this Thing.
*   **contains** is an array of Things that an instance of this Thing contains, specified by their name.
    *   For example, ["banana"] means this Thing contains exactly 1 instance of a banana. ["banana","orange"] means it contains 1 banana
        and 1 orange.
    *   ["banana","strawberry,25%"] means it will contain 1 banana, and has a 25% probability of also containing a strawberry.
    *   ["banana,2-7"] means it will contain between 2 and 7 bananas.
    *   [".banana"] will not include a banana in the Thing; instead, the Thing will contain whatever the banana normally contains.
    *   ["banana",["sugar","honey"]] will include a banana, and either sugar or honey. Unfortunately, this does not work with the format
        ".sugar" or ".honey".
*   **name_generator** is optional; if specified, the instance of the Thing will be named according to this.
    *   It can be either an array containing other arrays (the name will be patched up from an element of each array) or an identifier for
        the Name function, like *BOOK*.
    *   A name generator of [["blue ","red "],["frog","toad"]] will produce names such as "blue frog" or "red toad".

Inspired by: https://orteil.dashnet.org/nested
"""
# from .materials import FACTORIES as MATERIAL_FACTORIES
# from .universe import FACTORIES as UNIVERSE_FACTORIES
# from .life import FACTORIES as LIFE_FACTORIES


FACTORIES = {
    # **MATERIAL_FACTORIES,
    # **UNIVERSE_FACTORIES,
    # **LIFE_FACTORIES,
}
