"""
//basic materials and particles
//(these are very rough simplifications, don't hold all the inaccuracies against me)
"""
# Things.add_thing("diamond",["carbon"])
# # new Thing("oil",["lipids"]);
# Things.add_thing("magma",[".rock"])
# Things.add_thing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"])
# Things.add_thing("silica",["silicon","oxygen"]);
# # new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
# Things.add_thing("salt",["chlorine","sodium"])
# Things.add_thing("water",["hydrogen","oxygen"])
# # Things.add_thing("fire",["oxygen","carbon"])
# # Things.add_thing("ash",["organic matter","carbon"])
# # Things.add_thing("dew",["water"])
# Things.add_thing("ice",["water"])
# # Things.add_thing("snow",["snowflakes"])
# # Things.add_thing("snowflakes",["water"])
"""
new Thing("diamond",["carbon"]);
new Thing("oil",["lipids"]);
new Thing("magma",[".rock"]);
new Thing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"]);
new Thing("silica",["silicon","oxygen"]);
new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
new Thing("salt",["chlorine","sodium"]);
new Thing("water",["hydrogen","oxygen"]);
new Thing("fire",["oxygen","carbon"]);
new Thing("ash",["organic matter","carbon"]);
new Thing("dew",["water"]);
new Thing("ice",["water"]);
new Thing("snow",["snowflakes"]);
new Thing("snowflakes",["water"]);
"""


from .chemistry import *


# Things.from_contents(CHEMISTRY_CONTENTS)
# # alright, I'm not doing the whole periodic table.
# # Things.add_thing("proteins",[".molecule"])
# # Things.add_thing("lipids",[".molecule"])
# # Things.add_thing("glucids",["carbon","hydrogen","oxygen"],"glucose")
# # Things.add_thing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"])
"""
//alright, I'm not doing the whole periodic table.
new Thing("proteins",[".molecule"]);
new Thing("lipids",[".molecule"]);
new Thing("glucids",["carbon","hydrogen","oxygen"],"glucose");
new Thing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"]);
"""


from .particles import *


# Things.from_contents(PARTICLES_CONTENTS)
# # Things.add_thing("portal",["universe"])
"""
new Thing("portal",["universe"]);
"""



