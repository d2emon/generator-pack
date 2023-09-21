"""
//food
new Thing("milk",[
    GlucidsFactory.one(),
    LipidsFactory.one(),
    ELEMENTS['Ca'].one(),
]);
new Thing("bottle",[["glass",
    PlasticFactory.one(),
    "cardboard"],"label"]);
new Thing("glass bottle",["glass"],"bottle");
new Thing("glass jar",["glass"],"jar");
new Thing("label",["paper"]);
new Thing("milk bottle",[".bottle","milk"]);
new Thing("wine bottle",[".bottle","wine"]);
new Thing("wine",["sugar",
    AlcoholFactory.one(),
]);
new Thing("water bottle",[".bottle",
    WaterFactory.one(),
]);
new Thing("juice bottle",[".bottle","juice"]);
new Thing("soda bottle",[".bottle","soda"]);
new Thing("juice",[
    WaterFactory.one(),
    "sugar"],[["apple","pear","banana","tomato","pineapple","pumpkin","carrot","grape","orange","papaya","kiwi","mango"],[" juice"," juice"," juice"," smoothie"]]);
new Thing("soda",[
    WaterFactory.one(),
    "sugar"],[["apple","pineapple","grape","orange","purple","brown"],[" soda"]]);
new Thing("can",[
    WaterFactory.one(),
    "sugar","salt","mold,3%","metal"],[["canned "],["apple bits","pear bits","tomatoes","pineapple","pumpkin","carrots","meat","pork","beef","peas","mushrooms","olives","fish","burger","corn"]]);
new Thing("cookie box",["sugar","salt,70%","mold,3%","cardboard"],[["box of "],["cheesy","cheese","sugar","cream","milk","milky","whole-grain","frosted","glazed","apple","nut","fruit","chocolate","butter","oat","wheat","corn","animal-shaped","meat","crunchy","crispy"],[" "],["puffs","poofs","cookies","biscuits","rolls","pops","snacks","crackers","cereals","pies","tarts"]]);
new Thing("yeast",[".cell"]);
new Thing("yoghurt",["milk","sugar","yeast"],[["strawberry","vanilla","cherry","pear","plain"],[" yoghurt"]]);
new Thing("ice cream",["milk","sugar",
    IceFactory.one(50),
],[["strawberry","vanilla","cherry","chocolate"],[" ice cream"]]);
new Thing("cheese",["milk","yeast","mold,30%"],[["roquefort","cheddar","gouda","edam","colby","mozarella","processed cheese","stilton","goat cheese","gorgonzola","brie","camembert"]]);
new Thing("roast",[".meat","spices"],[["chicken","beef","pork","duck","mutton"],[" roast"]]);
new Thing("spices",
    (OrganicFactory.one()),
    [["pepper","garlic","onions","rosemary","sage","thyme"]]);
new Thing("meat",[
    BloodVesselsFactory.probable(5),
    BonesFactory.probable(5),
    FatFactory.probable(50),
    MusclesFactory.one(),
    SaltFactory.one(),
]);
new Thing("tomato sauce",[
    GlucidsFactory.one(),
    "meat,20%","salt"]);
new Thing("pasta",["salt",
    GlucidsFactory.one(),
    "cheese,5%","tomato sauce,20%"],["spaghetti","noodles","fusilli","fettuccine","fettuce","tagliatelle","cannelloni","penne","rigatoni","farfalle","tortelloni","ravioli","gnocchi"]);
new Thing("pastry",["sugar","salt","dough"],"pastry");
new Thing("pie",[["fruit jam","meat"],".pastry"],"pie");
new Thing("cake",[".pastry"],[["chocolate","white chocolate","chestnut","fruit","huge","impressive","ornate","glazed","colorful","cheese","nut","delicious"],[" cake"]]);
new Thing("fruit jam",["plant cell","sugar"]);
new Thing("donut box",["donut,0-12","cardboard"],"doughnut box");
new Thing("donut",[".pastry"],[["vanilla ","strawberry ","raspberry ","cherry ","chocolate ","coconut ","cream ","cinnamon ","bacon ","sprinkly ","frosted ","glazed ","powdered ",""],["doughnut"]]);
new Thing("sugar",[
    GlucidsFactory.one(),
]);
new Thing("dough",[
    GlucidsFactory.one(),
    LipidsFactory.one(),
]);
"""
