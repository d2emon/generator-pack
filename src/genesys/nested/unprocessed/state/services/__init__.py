"""
//services
new Thing("fire department",[
    FireFactory.probable(0.2),
    "firefighter,3-6","desk,0-3","chair,1-4","fridge,60%","tv,60%","fire truck",".building"]);
new Thing("firefighter",[
    (PersonFactory),
    ],"*PERSON*| (firefighter)");

new Thing("police station",["police officer,2-6","desk,0-2","tv,40%","small bookshelf,0-2","chair,0-4",".building"]);
new Thing("police officer",[
    (PersonFactory),
    ],"*PERSON*| (police officer)");

new Thing("library",["bookshelf,10-30","painting,50%","painting,50%","painting,50%","desk,0-4","computer,0-4","chair,0-4","librarian,1-4",
    PersonFactory.multiple(0, 12),
    ".building"]);
new Thing("librarian",[
    (PersonFactory),
    ],"*PERSON*| (librarian)");
"""
