"""
//war stuff
new Thing("battlefield",["soldier,10-30","Corpse,10-30","Blood"]);
new Thing("soldier",[".Person","arsenal","Blood,20%","bullet wound,0-3"],[["*PERSON*| "],["(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(officer)","(lieutenant)","(captain)","(major)"]]);
new Thing("arsenal",["gas mask,20%","rifle,90%","knife,80%","handgun,90%","handgun,50%","knife,30%","ammo pack,0-4","grenade,0-4","bullet,0-5"]);
new Thing("bullet",["Copper","Lead"]);
new Thing("rifle",["Steel","Aluminium,50%","Polymers,20%","bullet,0-6"]);
new Thing("handgun",["Steel","Aluminium,50%","Polymers,20%","bullet,0-6"]);
new Thing("gun",[".handgun"]);
new Thing("knife",["Steel","Blood,10%"]);
new Thing("wound",["Blood","worm,5%"],"wound");
new Thing("ammo pack",["bullet,0-20",["metal","Plastic"]]);
new Thing("grenade",["Iron","TNT",["metal","Plastic"]]);
new Thing("TNT",["Carbon","Hydrogen","Oxygen","Nitrogen"],"TNT");
new Thing("gas mask",["metal","Polymers","cloth"]);
new Thing("bullet wound",["Blood","worm,5%","bullet,50%","bullet,30%","bullet,10%","bullet,2%"],"wound");
"""
