"""
//[DATA EXPUNGED]
new Thing("research facility",["researcher,2-8","security guard,1-4","soldier,0-6","doctor,0-2","nurse,0-2",
    [
        CorpseFactory.multiple(0, 3),
        "",""
    ],"containment room,1-12","top secret drawer,1-6",".building"]);
new Thing("researcher",[
    (PersonFactory),
    ],"*PERSON*| (researcher)");
new Thing("security guard",[
    (PersonFactory),
    "handgun","ammo pack,0-1"],"*PERSON*| (security guard)");
new Thing("containment room",[
    [
        PortalFactory.one(),
        "space animal","space monster","sea monster","bird","poultry","cat","dog","cetacean","fish","mollusk","plankton","reptile","amphibian","snake","small mammal","predatory mammal","herbivorous mammal","clam","worm","monkey","bear","shark","horse","insect","crustacean","dragon",
        PersonFactory.one(),
        "ghost","ectoplasm","abomination",
        CorpseFactory.one(),
        "house","tree","machine","dinosaur","visitor","visitor furniture","medieval person","caveman","painting","","",""
    ],
    PortalFactory.one().probable(1),
    FireFactory.probable(1),
    "researcher,5%","researcher,5%","soldier,5%","soldier,5%",
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    ]);
new Thing("top secret drawer",["top secret folder,1-8","note,0-8","pen,30%","pen,10%","pen,5%","donut box,5%","can,2%","book,20%","book,20%","book,5%","book,5%","button,10%","button,10%","dust,60%","lint,40%"],"classified files");
new Thing("top secret folder",["top secret file,2-8","paper"],[["Classified Folder n°"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"]]);
new Thing("top secret file",[],[
["File ","Document ","Report "],["X","Z","A","B","L","S","T"],["-"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"],["<br>-"],
["Containment breach ¤¤¤","Subject ¤¤¤ attempted escape","Unusual events occuring","Possible breach of security measures in","Subject ¤¤¤ sighted","Witnesses report a ¤¤¤","Rumors of ¤¤¤","Singularity event","Subject ¤¤¤ attempted singularity","Retrieval of subject ¤¤¤","Accidental termination of subject ¤¤¤","Recovery of subject ¤¤¤","Recovery of a number of ¤¤¤","Accidental loss of ¤¤¤","New leads on ¤¤¤","Subject ¤¤¤ must now be kept away from ¤¤¤ at all times to avoid repeating the security breach that occurred","Locals report sightings of ¤¤¤","Subject ¤¤¤ transported","A number of ¤¤¤ were sighted","Subject ¤¤¤ has been predicted to have been","Retrieving supplies","Accidental destruction of all subjects","Retrieval of artifact ¤¤¤","Sightings of artifact ¤¤¤","Subject ¤¤¤ tried to merge with ¤¤¤","Subject ¤¤¤ sighted with artifact ¤¤¤","Experimentation done on ¤¤¤","Research ongoing on ¤¤¤","True nature of ¤¤¤ revealed","Gate to ¤¤¤ opened","Portal to ¤¤¤ closed","Relations friendly with ¤¤¤","Relations hostile with ¤¤¤","A team has been sent to investigate ¤¤¤","No news from the team sent to","Mission ¤¤¤ presumed to have been a failure; no further teams should be sent","Met with subject ¤¤¤","Artifact ¤¤¤ damaged but not destroyed","Artifact ¤¤¤ suspected to have been destroyed","Subject ¤¤¤ presumed dead","Subject ¤¤¤ unfortunately still alive","Phenomenons possibly caused by ¤¤¤ spotted","Phenomenons matching ¤¤¤'s behavior have been observed","Discussions on the whereabouts of ¤¤¤ took place","Subject ¤¤¤ travelled from ¤¤¤ to ¤¤¤","Subject ¤¤¤ sighted shape-shifting from a ¤¤¤ to a ¤¤¤","Subject ¤¤¤ started duplicating","Subject ¤¤¤ resumed duplicating","Subject ¤¤¤ will have/has started to ¤¤¤","Collision event between ¤¤¤ and ¤¤¤","Evidence of ¤¤¤"],[" "],
["in sector","in zone","in secured location","in facility","near site"],[" "],["X","Z","A","B","L","S","T"],["-"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"],[" "],
["on ¤¤/¤¤/¤¤¤¤","the day preceding ¤¤¤","following the ¤¤¤","in the hours leading to the ¤¤¤ event","in the hours following the ¤¤¤ event","directly after ¤¤¤","during the ¤¤¤ event"],
["; all researchers involved terminated","; all personnel involved terminated","; casualties estimated high to very high","; no casualties reported","; proper measures have been triggered","; more research is necessary","; further testing still needed","; casualties include half the local population","; casualties include all local wildlife",". Once again, do not, I repeat DO NOT ¤¤¤",". Do not, under any circumstances, attempt to ¤¤¤","; locals have been terminated","; locals have no memory of the event","; consequences of the event have been dealt with","","","","","",""],["."]
]);
"""
