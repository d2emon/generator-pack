//war stuff
new Thing("battlefield",["soldier,10-30","corpse,10-30","blood"]);
new Thing("soldier",[".person","arsenal","blood,20%","bullet wound,0-3"],[["*PERSON*| "],["(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(officer)","(lieutenant)","(captain)","(major)"]]);
new Thing("arsenal",["gas mask,20%","rifle,90%","knife,80%","handgun,90%","handgun,50%","knife,30%","ammo pack,0-4","grenade,0-4","bullet,0-5"]);
new Thing("bullet",["copper","lead"]);
new Thing("rifle",["steel","aluminium,50%","polymers,20%","bullet,0-6"]);
new Thing("handgun",["steel","aluminium,50%","polymers,20%","bullet,0-6"]);
new Thing("gun",[".handgun"]);
new Thing("knife",["steel","blood,10%"]);
new Thing("wound",["blood","worm,5%"],"wound");
new Thing("ammo pack",["bullet,0-20",["metal","plastic"]]);
new Thing("grenade",["iron","TNT",["metal","plastic"]]);
new Thing("TNT",["carbon","hydrogen","oxygen","nitrogen"],"TNT");
new Thing("gas mask",["metal","polymers","cloth"]);
new Thing("bullet wound",["blood","worm,5%","bullet,50%","bullet,30%","bullet,10%","bullet,2%"],"wound");