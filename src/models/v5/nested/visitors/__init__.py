"""
//visitors
new Thing("visitor",["visitor body","visitor psyche"],"visitor");
new Thing("visitor body",["visitor head","visitor head,2%","visitor torso","visitor arm,99%","visitor arm,2%","visitor arm,99%","visitor leg,99%","visitor leg,99%","visitor leg,2%"],"body");
new Thing("visitor torso",["visitor chest","visitor pelvis",".BodyPart"],"torso");
new Thing("visitor chest",[".BodyPart"],"chest");
new Thing("visitor pelvis",["visitor naughty bits",".BodyPart"],"pelvis");
new Thing("visitor naughty bits",[".SoftBodyPart"],["thrusher"]);
new Thing("visitor arm",["visitor hand","visitor elbow,2","visitor armpit",".BodyPart"],"arm");
new Thing("visitor hand",["visitor finger,3",".BodyPart"],"hand");
new Thing("visitor finger",[".BodyPart"],"finger");
new Thing("visitor elbow",[".BodyPart"],"elbow");
new Thing("visitor armpit",["visitor ooze,70%",".SoftBodyPart"],"armpit");
new Thing("visitor leg",["visitor foot","visitor knee",".BodyPart"],"leg");
new Thing("visitor foot",["Toe,4","visitor ooze,40%",".BodyPart"],"foot");
new Thing("visitor toe",[".BodyPart"],"toe");
new Thing("visitor knee",[".BodyPart"],"knee");
new Thing("visitor head",["visitor mouth","Eye,0-4","Skull"],"head");
new Thing("visitor eye",["EyeFlesh","visitor ooze,20%"],"eye");
new Thing("Nose",["Nostril,2",".BodyPart"],"nose");
new Thing("visitor mouth",["visitor teeth","Tongue,2","visitor ooze"],"mouth");
new Thing("visitor teeth",["Steel"],"teeth");
new Thing("visitor ooze",["bacteria,40%","OrganicMatter","Sulfur"],"ooze");

new Thing("visitor psyche",["visitor thoughts","visitor memories"],"psyche");
new Thing("visitor thoughts",["visitor thought,1-3"],"thoughts");
new Thing("visitor memories",["visitor memory,1-2"],"memories");
new Thing("visitor thought",[],["ACK!!! ACK ACK ACK","ACK ACK AAAACK ACK ACK","ACK, ACKKKKKKKK","AAAAAAAAAACKKKKKKK","Ack.","Ack?","Ack... Ack ack ack.","Ack ack ock ack!","Ack eck.","Ack ACK AAAAACK","AACK, ACK ACK ACK!","AAAAACK ACK ACK ACK","ACKACKACK, ACK!!!","Ackack, ackackackack?","...ack...","Hehuck.","Whoack."]);
new Thing("visitor memory",[],[["Ack ack...","Ack, ack ack...","Ack.","...Ack ack.","Ack ack ack."],["",""," Ack ack ack ack."," Ack."," Ack, ack ack."," Ack ack ack..."," ...ack ack ack."," ...Ack."," Ack."]]);

new Thing("named visitor",[".visitor"],[["B"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","?",";",",",".",":","/","*","#","¤","+","-","="," "],["rt"],["y","ie","ington","inson","son","","","","","","",""]]);

new Thing("visitor city",["named visitor,0-8",["space animal,0-3",""],"visitor neighborhood,1-8"],"visitor city");
new Thing("visitor neighborhood",["named visitor,0-8",["space animal,0-3",""],"visitor building,2-16"],"neighborhood");
new Thing("visitor building",[["named visitor,0-8",""],"visitor room,1-8"],[["a tall","a wide","a spiralicious","a twisty","a holographic","a composite","a stout","a long","a domed","an underground","a submerged","a gigantic"],[", "],["green","blue","purple","white","gray","translucent","bright","porous","microsthetic","turbified","motorized","hovering","meshed","towered","automated","ridged"],[" "],["glumporium","swapmarket","slickmarket","juicehouse","scienceteria","faceteria","homezone","orbshop","oozeshop","marklorion","hive","holotekt"]]);
new Thing("visitor room",["named visitor,60%","named visitor,30%","named visitor,10%","named visitor,10%","named visitor,10%","space animal,10%","visitor furniture,1-6",".room"],"room");
new Thing("visitor furniture",["Abomination,1%","space animal,3%","named visitor,2%","organic matter,5%",["glass","metal","concrete","Plastic"]],[["symbio","opto","auto","synchro","thru","ato","ecto","diplo","plasti","pasta","pluta","elu","gubri","capra","lubio","logi","plato","micro","alto","tele","meta","anti","poly","mono","corvo"],["shid","synth","shaver","shist","mizer","mucus","twister","ridger","cutter","mac","maker","ctory","ctamid","chton","leaker","grater","board","frame","table","stand","plug","masher","greeter","mobile","pin","vat","tron","drone","chron","tub","fridge","pool","box","cube","morpher","phraser"]]);
new Thing("visitor installation",["named visitor,0-4",["space animal,0-3",""],"visitor building,1-3"],[["pod","grub","egg","limb","ooze","tendril","bulb","pulp","energy","smoke","hive","moisture","cat"],[" "],["materializer","synthesizer","factory","farm","collector","cultures","pit","fields","crops","barn","vat"]]);
new Thing("visitor ship",["named visitor,1-3","Person,20%","space animal,30%","visitor furniture,1-6","metal"],"visitor UFO");
"""
