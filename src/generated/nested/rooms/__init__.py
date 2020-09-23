"""
//rooms
new Thing("building",["walls","roof"]);
new Thing("roof",["cat,2%","bird,10%","bird,10%","nest,2%","roof tiles"]);
new Thing("roof tiles",["ceramic"],"tiles");
new Thing("room",["visitor,0.1%","ghost,0.1%","walls"]);
new Thing("walls",["door,1-4","window,0-6",["wall,4","wall,4-8"]]);
new Thing("wall",[["plaster","wood"],"dirt,5%"]);
new Thing("plaster",["calcium","sulfur"]);
new Thing("marble",["calcium"]);
new Thing("stone",["rock"]);
new Thing("concrete",["rock","cement","water"]);
new Thing("cement",["calcium"]);
new Thing("marble",["calcium"]);
new Thing("door",["wood frame","glass,10%"]);
new Thing("window",["wood frame","glass"]);
new Thing("living-room",[".room","person,0-4","cat,10%","cat,10%","stuff box,5%","tv,95%","armchair,50%","armchair,50%","couch,90%","living-room table,50%","chair,1-6","painting,70%","painting,20%","mirror,2%","bookshelf,0-3","small bookshelf,0-2","desk,40%","computer,40%"]);
new Thing("kitchen",[".room","person,40%","person,20%","tv,40%","kitchen sink","cabinet,1-5","fridge","oven","chair,0-3","computer,5%","small bookshelf,5%","painting,30%","painting,10%"]);
new Thing("bedroom",[".room","person,40%","person,10%","cat,5%","stuff box,5%","tv,60%","bed","chair,0-4",["cupboard,90%","closet,90%"],"mirror,50%","bookshelf,0-2","small bookshelf,0-3","desk,40%","computer,40%","painting,60%","painting,20%"]);
new Thing("bathroom",[".room","person,10%","person,1%","cat,1%","sink,95%",["bathtub","shower"],"toilet","painting,20%","mirror,80%"]);
new Thing("study",[".room","person,30%","person,5%","stuff box,20%","tv,20%","desk,95%","computer,90%","chair,1-4","bookshelf,0-6","painting,70%","painting,20%","mirror,5%"]);
new Thing("garden",["person,40%","person,10%","dog,20%","dog,5%","cat,15%","grass","tree,50%","tree,50%","tree,20%","tree,5%","flowers,30%","hole,1%","hole,1%","hole,1%","poultry,1%","bird,20%","bird,10%"],["garden","lawn","backyard"]);
new Thing("garage",["person,20%","cat,2%","stuff box,30%","stuff box,20%","chair,0-3","car,90%","car,40%","car,5%","bike,40%","bike,30%","bike,10%","computer,5%","small bookshelf,30%","hole,1%","hole,0.5%","small mammal,5%","insect,15%","insect,15%","dirt,50%"]);
new Thing("hole",["corpse,20%","corpse,5%","blood,20%","shovel,20%","hole,0.5%","insect,25%","insect,15%","dirt"]);
"""