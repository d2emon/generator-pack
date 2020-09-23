# How to add a new Thing :
#   new Thing(name,contains,name generator);
#       -name is the referral name for this Thing. Unless a name generator is specified, this name will be the default
#           name for any instances of this Thing.
#       -contains is an array of Things that an instance of this Thing contains, specified by their name.
#           -For example, ["banana"] means this Thing contains exactly 1 instance of a banana. ["banana","orange"]
#               means it contains 1 banana and 1 orange.
#           -["banana","strawberry,25%"] means it will contain 1 banana, and has a 25% probability of also containing a
#               strawberry.
#           -["banana,2-7"] means it will contain between 2 and 7 bananas.
#           -[".banana"] will not include a banana in the Thing; instead, the Thing will contain whatever the banana
#               normally contains.
#           -["banana",["sugar","honey"]] will include a banana, and either sugar or honey. Unfortunately, this does
#               not work with the format ".sugar" or ".honey".
#       -name generator is optional; if specified, the instance of the Thing will be named according to this.
#           It can be either an array containing other arrays (the name will be patched up from an element of each
#               array) or an identifier for the Name function, like *BOOK*.
#           A name generator of [["blue ","red "],["frog","toad"]] will produce names such as "blue frog" or "red toad".

from ..materials import *
from .universe import *
from .cell import *
from .body import *
from .brain import *
from .cloth import *
from .terrain import *
from .vegetation import *
from .life import *
from .world_subdivisions import *
from .towns import *
from .buildings import *
from .farms import *
from .offices import *
from .small_shops import *
from .museums import *
from .services import *
from .war_stuff import *
from .hospitals import *
from .data_expunged import *
from .cemeteries import *
from .infrastructure import *
from .rooms import *
from .furniture import *
from .computers import *
from .food import *
from .visitors import *
from .medieval_and_ancient import *
from .medieval_people import *
from .medieval_towns import *
from .dungeons import *
from .future_stuff import *
from .caveman_stuff import *
from .meta import *

# to add :

# cows, fungi, more shops, temples, more buildings, paintings, internal organs, phones, lamps, abandoned plants/castles,
# spaceships oh god

# actual battlefield thoughts, military bases, ships, airports, more street names, space ships/stations,
# giant colony ships, wasteland worlds, cults, space probes, prisons, government buildings, schools, amphibian skin

