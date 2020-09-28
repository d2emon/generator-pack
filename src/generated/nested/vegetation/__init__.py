"""
//vegetation
new Thing("plant cell",[".Cell"],["plant cells"]);
new Thing("grass",["grass blade,50-100"]);
new Thing("grass blade",["grass thoughts,2%","Dew,6%","worm,3%","insect,6%","plant cell"]);
new Thing("grass thoughts",["grass thought,1"],"thought");
new Thing("grass thought",[],[":D",":O","D:",":|",":]",">:0"]);
new Thing("trees",["tree,20-50"]);
new Thing("tree",["tree thoughts,2%","tree trunk","branches","leaves","nest,5%","nest,2%","fruits,20%","flowers,20%"],["larch","fir","oak","birch","pine","sequoia","cedar","spruce","ash","poplar","elm","sycamore","willow","mahogany","laurel","orange tree","lemon tree","palm tree","coconut tree","pear tree","apple tree","walnut tree","olive tree"]);
new Thing("tree thoughts",["tree thought,1"],"thought");
new Thing("tree thought",[],["Well. What is this all about.","So. What's the hurry?","Whoah. Slow down.","Do like a tree. And go away.","I seen some things.","They're coming.","We know.","We've been watching you for hundreds of years.","Do you have any idea how old I am?","Yes. I remember you. I remember all of you."]);
new Thing("leaves",["leaf,50-100"]);
new Thing("leaf",["Dew,6%","insect,6%","plant cell"]);
new Thing("branches",["branch,10-30"]);
new Thing("branch",["insect,6%","leaf,10%","plant cell"]);
new Thing("twig",["plant cell"]);
new Thing("fruits",["worm,5%","plant cell","sugar"]);
new Thing("flowers",["insect,5%","plant cell","pollen"]);
new Thing("pollen",["plant cell","sugar"]);
new Thing("tree trunk",["insect,4%","wood","bark"]);
new Thing("bark",["insect,10%","worm,10%","wood"]);
new Thing("jungle trees",["jungle tree,20-150"],"trees");
new Thing("jungle tree",[".tree"],["tree"]);
new Thing("humus",["insect,0-3","worm,0-3","twig,0-3","leaf,0-6","OrganicMatter","dirt"]);
new Thing("nest",["bird,50%","egg shell,20%","bird egg,0-6","twig,6-12"]);

"""