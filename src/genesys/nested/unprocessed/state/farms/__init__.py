"""
//farms
new Thing("farm",[
    FireFactory.probable(0.3),
    "house,1-3","farmer,1-4","field,1-8","horse,30%","horse,30%","horse,30%","poultry,0-3","grain silo,0-2","barn,0-2","warehouse,0-2","storage shed,0-2"]);
new Thing("field",["grain","insect,5%","bird,10%","bird,5%","haystack,30%"],["wheat field","corn field","soy field","rice field","oat field","peanut field","tomato field","grape field","barley field","canola field","rye field","flower field"]);
new Thing("farmer",[".person"],"*PERSON*| (farmer)");
new Thing("grain",["plant cell"]);
new Thing("grain silo",["metal","grain"]);
new Thing("warehouse",["worker,0-2","small mammal,8%","ghost,0.3%","machine,0-4",".building"]);
new Thing("barn",[".building"]);
new Thing("storage shed",[".building"]);
new Thing("haystack",["grain","insect,10%","needle,0.1%"]);
new Thing("needle",["metal"]);

new Thing("factory",["worker,2-12","machine,1-12","pipes,40%","cables,0-1","public bathroom,60%","warehouse,0-2",".building"],[["toy","chocolate","car","yoghurt","processed food","pork products","canned beef","juice","soda","shoe","textile","computer","weapon","hardware"],[" factory"]]);
new Thing("worker",[".person"],"*PERSON*| (worker)");

new Thing("public bathroom",[".room","person,10%","person,1%","sink,1-4","toilet,1-4","mirror,0-3"],"restroom");
"""
