"""
//rooms
new Thing("building",["walls","roof"]);
new Thing("roof",["cat,2%","bird,10%","bird,10%","Nest,2%","roof tiles"]);
new Thing("roof tiles",["ceramic"],"tiles");
new Thing("room",["visitor,0.1%","ghost,0.1%","walls"]);
new Thing("walls",["door,1-4","window,0-6",["wall,4","wall,4-8"]]);
new Thing("wall",[["plaster","wood"],"dirt,5%"]);
new Thing("plaster",["Calcium","Sulfur"]);
new Thing("marble",["Calcium"]);
new Thing("stone",["Rock"]);
new Thing("concrete",["Rock","cement","Water"]);
new Thing("cement",["Calcium"]);
new Thing("marble",["Calcium"]);
new Thing("door",["wood frame","glass,10%"]);
new Thing("window",["wood frame","glass"]);
new Thing("living-room",[".room","Person,0-4","cat,10%","cat,10%","stuff box,5%","tv,95%","armchair,50%","armchair,50%","couch,90%","living-room table,50%","chair,1-6","painting,70%","painting,20%","mirror,2%","bookshelf,0-3","small bookshelf,0-2","desk,40%","computer,40%"]);
new Thing("kitchen",[".room","Person,40%","Person,20%","tv,40%","kitchen sink","cabinet,1-5","fridge","oven","chair,0-3","computer,5%","small bookshelf,5%","painting,30%","painting,10%"]);
new Thing("bedroom",[".room","Person,40%","Person,10%","cat,5%","stuff box,5%","tv,60%","bed","chair,0-4",["cupboard,90%","closet,90%"],"mirror,50%","bookshelf,0-2","small bookshelf,0-3","desk,40%","computer,40%","painting,60%","painting,20%"]);
new Thing("bathroom",[".room","Person,10%","Person,1%","cat,1%","sink,95%",["bathtub","shower"],"toilet","painting,20%","mirror,80%"]);
new Thing("study",[".room","Person,30%","Person,5%","stuff box,20%","tv,20%","desk,95%","computer,90%","chair,1-4","bookshelf,0-6","painting,70%","painting,20%","mirror,5%"]);
new Thing("garden",["Person,40%","Person,10%","dog,20%","dog,5%","cat,15%","Grass","Tree,50%","Tree,50%","Tree,20%","Tree,5%","Flowers,30%","hole,1%","hole,1%","hole,1%","poultry,1%","bird,20%","bird,10%"],["garden","lawn","backyard"]);
new Thing("garage",["Person,20%","cat,2%","stuff box,30%","stuff box,20%","chair,0-3","car,90%","car,40%","car,5%","bike,40%","bike,30%","bike,10%","computer,5%","small bookshelf,30%","hole,1%","hole,0.5%","small mammal,5%","insect,15%","insect,15%","dirt,50%"]);
new Thing("hole",["Corpse,20%","Corpse,5%","Blood,20%","shovel,20%","hole,0.5%","insect,25%","insect,15%","dirt"]);
"""