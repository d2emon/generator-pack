"""
//small shops
new Thing("shop",["clerk,1-6",["customer,0-3","customer,0-15"],"desk,1-3","chair,0-3","tv,20%","warehouse,20%",".building"]);
new Thing("clerk",[".person"],"*PERSON*| (clerk)");
new Thing("customer",[".person"],"*PERSON*| (customer)");

new Thing("game shop",["video game stand,2-12","video game console,1-4","tv,1-3","computer,0-3",".shop"],[["Game","Gamer","Play"],["pro","shop","hub","go","cash","buy","now","grrrlz","bro","chump"]]);
new Thing("video game stand",["video game,2-20","plastic"],"video game stand");
new Thing("fresh produce shop",["produce stall,2-12",".shop"],[["Fresh","Green","Bio","Nature","Eco","Yum","Tasty"],["Produce","Froots","Fruits","Veggies","Vegetables","Life","Food"]]);
new Thing("produce stall",[["fruit pile,1-4","vegetable pile,1-4"],"glass","plastic","insect,10%"],"produce stall");
new Thing("fruit pile",["sugar","plant cell","insect,10%"],[["a pile of "],["apples","oranges","pears","figs","watermelons","bananas","kiwis","coconuts","lemons","limes","strawberries","raspberries","berries","blackberries","nuts","grapes","grapefruits","melons","peaches","apricots","pineapples","cherries","chestnuts","ginger","mangos","passion fruits","mangosteens","plums","lychees","kumquats","tangerines","rhubarb","durians","mulberries"]]);
new Thing("vegetable pile",["plant cell","insect,10%"],[["a pile of "],["potatoes","carrots","leeks","onions","garlic","spices","turnips","cabbages","lettuce","corn cobs","spinach leaves","cress","broccoli","kale","peas","radish","beets","tomatoes","cucumbers","zucchinis","peppers","eggplants","gourds","pumpkins","avocados","cauliflowers","artichokes","fava beans","beans","green beans","chickpeas","peanuts","soybeans","celery","asparagus","rutabagas","yams","olives"]]);//I'm putting tomatoes with vegetables and you can't stop me
new Thing("pet shop",["pet container,2-12","bird cage,1-6","vivarium,1-6","aquarium,1-6",".shop"],[["Pet","Cute","Adopt","Ani","Anima","World","Care","Woof","Meow","Purr"],["woof","meow","purr","dogz","catz","nimals","friends"]]);
new Thing("pet container",[["dog,1-4","cat,1-4"],"plastic"],["pet cage","pet box"]);
new Thing("vivarium",[["reptile,1-4","amphibian,1-4","insect,1-4"],"plastic","glass","dirt"]);
new Thing("aquarium",[["fish,1-6","cnidaria,1-4","mollusk,1-4","crustacean,1-4"],["fish,50%","cnidaria,50%","mollusk,50%","crustacean,50%"],"plankton,0-3","plastic","glass",
    WaterFactory.one(),
]);
new Thing("bird cage",["bird","plastic","metal"]);
new Thing("toy shop",["toy box,2-12","video game console,40%","video game console,20%",".shop"],[["Toy","Play","Kidz","Yay","Magi","Super","Cosmo"],["time","pretend","play","toyz","dolls","blocks","stuff","fun"]]);
new Thing("toy box",["office toy,20%","office toy,20%","toy,0-8","doll,0-4"]);
new Thing("toy",[["wood","plastic"]],["spinning top","building blocks","construction set","castle playset","city playset","village playset","animal playset","dinosaur playset","wizard playset","family playset","warrior playset","underwater playset","cow-boy playset","space playset","figurines","chef playset","market playset","toy car","toy racing car","race tracks","boat model","airplane model","spaceship model"]);
new Thing("doll",["plastic","cloth"],[["robot","trendy","fashion","cyborg","nurse","chef","firefighter","police","construction worker","singing","dancing","talking","super","baby-care","shopkeeper","knight","action hero","wizard","gardener","science","movie","TV","reporter","alien","cosmonaut","rocket","future","time-travel","ice-cream","lovely","romance","radical","pretend","plastic","mutant"],[" "],["Cindy","Stacy","Barbara","Lois","Milly","Emily","Anette","Gordon","Brandon","Steve","Marcus","Pascal","Barney","Boris","baby","unicorn","dragon","dinosaur","monster","pony","teddy bear","cat","dog","bunny","bird","shark"]]);
new Thing("bargain shop",["stuff box,2-12",".shop"],[["Cheap","Haggle","Price","Poor","Cent","Money","Best","Save","Get","Found","Salvage","Dump"],["more","less","buy","shark","bargain","stuff","things","worth","shop","store","market","mart"]]);
new Thing("stuff box",["office toy,0-2","souvenir,20%","book,0-2","pants,20%","shirt,20%","underwear,20%","coat,20%","socks,20%","shoes,20%","hat,20%","glasses,20%","toy,0-2","doll,30%","video game console,10%","video game console,10%","cog,30%","cog,10%","unusual stone,1%","helmet,1%","armor,1%","medieval weapon,1%","painting,20%","painting,10%","dust,40%","insect,10%"]);
new Thing("souvenir shop",["souvenir,6-12",".shop"],["souvenir shop","gift shop"]);
new Thing("souvenir",[["wood","plastic","metal","glass"]],[["tower","pyramid","dome","bridge","statue","palace","castle","cathedral","arena","opera","ark","city","monument"],[" "],["model","replica","souvenir"]]);
"""
