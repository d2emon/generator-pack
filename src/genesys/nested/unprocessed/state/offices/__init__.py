"""
//offices
new Thing("building hall",["office worker,0-3","elevator,1-3","public bathroom,75%"],"entrance hall");
new Thing("elevator",["ghost,0.3%","office worker,0-3","metal","cables","mechanics"]);
new Thing("office",["office worker,0-3","cat,2%","meeting room,0-2","boss's office","cubicle,2-12","water cooler,0-2","public bathroom,75%","elevator"],[["Social","Web","Swift","Smart","Smooth","Huge","Large","Greed","Bank","Media","World","Smith","Channel","Stock","Dream","One","True","We","You","People","Planet","Wild","Standard","Ever","Quick","Fast","Real","Good","Great","Neat","Soft","Hard","Right","Evil","Okay","Nice","Mascot","Clever","Green","Blue","White","Black","Time","Century","Millenium","NotCorrupt","PrettyAlright","PrettyDamnGood","Actual","Apex","Nested","Star","Opti","General","Easy","What","Who","Where","This","That","Dat","Dem","Invest","Painless","Death","First","Shark","Bear","Truth","Trust","Venture","Swell","Kind","Myth","Mythic","Crown","Silver","Gold","Twin","Single","Double","Triple","Marvel","Wonder","Way","Ward","e","I"],["co","alys","isium","arium","orium","orius","arius","aria","oria","arion","orion","ilton","son","cube","Monkey","Dog","Century","Year","TV","Big","Money","Rich","Bucks","Axis","Venture","Fine","Universal","Pro","Unlimited","brothers","Tube","Grow","Friends","Planet","People"," People"," Plastics"," Fashion"," Trending"," TV"," Games"," Toys"," Video Games"," Video"," Sports"," Pets"," Social"," Websites"," Marketing"," Sales"," Trading"," Export"," Politics"," Strategy"," Health"," Medecine"," Gardening"," Agriculture"," Editions"," Mining"," Transports"," Voyages"," Tourism"," Art"," Assassinations"," Healthcare"," Software"," Hardware"," Automobile"," Care"," Education"," Security"," Security Systems"," Crafts"," Production"," Services","Blood"," Space"," Transfer"," Backup"," Resources"," Secret Research"," Banking"," Funding"," Gambling"," Law"," Lawyers"," Pictures"," Religion"," Goods"," Weapons"," Laundering"," Cartoons"," Comics"," Agronomics"," Ergonomics"," Economics"," Supplies"," Things"," Stuff"," Printing"," Architecture"," Landscaping"," Construction"," Railroads"," Engineering"," Science"," News"," Testing"," Appliances"," Standards","Studio"," Recording"," Enrichment"," Extraction"," Frivolities"," Realty"," Publishing"," Entertainment"," Propane"," Energy"," Business Solutions"," Councelling"," Event-planning"," Fundraising"," Electronics"," Electrics"," Records"," Slavery"," Distribution"," Distributors"," Accessories"," Fuels"," Motors"," Insurance","Corp"," Procedurals"],[" "],["Inc.","Corp.","Company","L.P.","Ltd.","L.L.C.","L.C.","Associates","Partners","United","Merger","& Co","International","Conglomerate"]]);
new Thing("office worker",[".person"],"*PERSON*| (employee)");
new Thing("office boss",[".person"],"*PERSON*| (boss)");
new Thing("cubicle",["office worker,80%","office worker,10%","computer","computer,10%","small bookshelf,30%","fridge,2%","nameplate,8%","calendar,20%","office toy,0-3","desk","chair","panel,2-3"]);
new Thing("boss's office",["office boss","office worker,10%","office worker,5%","computer","computer,10%","water cooler,10%",["bookshelf","small bookshelf"],"cupboard,0-2","fridge,20%","nameplate","calendar,80%","office toy,0-6","desk","armchair,50%","chair,2-4","tv,10%"]);
new Thing("meeting room",["office boss,2%","office worker,0-8","cat,2%","computer,30%","computer,10%","water cooler,40%",["bookshelf","small bookshelf"],"cupboard,0-2","fridge,20%","nameplate,0-4","calendar,50%","office toy,0-6","table","chair,4-12","tv,60%"]);
new Thing("office toy",[
    PlasticFactory.one(),
    "metal"],["colorcube","colorsnake","snowglobe","figurine","souvenir","toy magnet","kinetic toy","bobblehead","spinning top","executive ball clicker","bouncing ball","slinky","stress ball","magic 8-ball","yo-yo"]);
new Thing("panel",[
    PlasticFactory.one(),
]);
new Thing("calendar",["paper","ink"],[["calendar ("],["firemen","sexy athletes","half-naked ladies","kittens","puppies","ducklings","flowery nature","tourism","sharks","inspirational quotes","famous people","bears","funny cartoons","popular TV show characters","mayan","haikus","1-word-a-day"],[")"]]);
new Thing("nameplate",[[
    PlasticFactory.one(),
    "wood","metal"]]);
new Thing("water cooler",[
    PlasticFactory.one(),
    WaterFactory.one(),
    "push-button"]);
"""
