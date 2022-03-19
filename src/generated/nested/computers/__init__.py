"""
//computers
new Thing("pixel paragraph",["pixel character,50-300"],"paragraph");
new Thing("pixel character",["bit,8"],"*CHAR*");
new Thing("computer",["computer screen","computer keyboard","computer mouse","electronics"],[["P","B","M","N","T","St","Pl","Bl","Gr","Fr","Sht","Fl"],["apple","indows","inux","oogle"],[" computer"]]);
new Thing("laptop",[".computer"],[["P","B","M","N","T","St","Pl","Bl","Gr","Fr","Sht","Fl"],["apple","indows","inux","oogle"],[" laptop"]]);
new Thing("computer keyboard",["Plastic","electronics"],"keyboard");
new Thing("computer mouse",["Plastic","electronics"],"mouse");
new Thing("computer screen",["internet browser","computer folder,1-4","software,0-4","video game,0-4","computer trashbin","Plastic","electronics"],"screen");
new Thing("computer folder",["computer folder,0-2",["computer folder,0-6","disturbing computer image,1-10","stupid computer image,1-10","cute computer image,1-10","software,1-6","video game,1-6"]],[["/"],["my ","My ","misc ","Misc. ","various ","secret ","family ","Family ","shared ","Shared ","important ","Important ","public ","Public ","private ","Private ","","",""],["documents","docs","Documents","Songs","Music","Movies","Pictures","pictures","pics","photos","files","Files","things","stuff","stuff to sort"]]);
new Thing("computer trashbin",["computer folder,0-4","disturbing computer image,0-4"],"Trashbin");
new Thing("video game",[".computer file"],[
["Super ","Mega ","Ultra ","Final ","World of ","","","","",""],
["Bl","B","Fl","Gl","Z","Zw","Dw","M","W","Wh","C","F","G","Pl","Spl"],["ario","antasy","and","astle","ark","ork","org","urg","ink","arf","ine","ar","at","uster","aster","alaxy","ims","ultima","universe","izzard"],
["craft","vania","arria","arium","'s Revenge","'s Quest"," Bros"," Town"," Land"," World"," Party"," Quest"," RPG"," Horses"," Friends"," Girlz"," Online"," Fantasy"," Ultra"," Deluxe"," Fortress"," Racing"," Edit"," Maker"," Beta"," Trial"," Music"," Ultimate"," Resurrection"," The Movie : The Game"," 2"," 3"," II"," III"," 2000"," 3000"," GOTY Edition"," Deluxe Edition"," expansion pack"," [keygen]"," [CRACK]"," HD","","","","","","","","","","",""]
,[".soft"]
]);
new Thing("software",[".computer file"],[
["Photo","Touch","Pic","Morph","Kid","Cosmo","Astro","Ink","Web","Art","Movie","Music","Calc","Math","Phrase","Dictio","World","Bug","Shell","Folder","File","Program","Question","EZ","Easy","Ancestry","History","Encyclo","Sun","Speed","Health","Doc","School","Learn","Lang","Code","Prog","Note","Pixel","Simple","Line","Shape","Name","Phone","Insta","Love","Friend","Assist","Tut","Active","Micro","Macro","Shock","Laser","Disc","Index","Game","Trouble","Hobbie","House","Task","Sports","Car","Money","Finance","Password","Fun","Mail","Virus","Fire","Burn","Diet","Pet","Mission","Hyper","Flower","Biblio","Video","Party","Open","Closed","Magic"],
["shop","pic","pix","draw","thinker","brain","pad","glide","top","artist","words","writer","layer","net","nary","matic","ulator","ula","ulus","ify","izer","crusher","finder","find","sort","reply","info","pro","pedia","helper","creator","card","land","warrior","armor","wall","nova","manager","paint","pixel","namer","call","book","tales","media","wave","mail","-b-gone","care","serve","server","printer","designer","retriever","spy","link","Office","cracker","Edit","Editor"],
[" Pro"," - More Clipart edition"," Assistant"," Fusion"," Easy"," Plus"," Professional"," Gold"," extended edition"," Free"," freeware version"," trial"," shareware"," Web"," Online"," Edit"," Illustrated"," 2.0"," 1.1"," 1.2"," 3.0"," [keygen]"," [CRACK]"," HD","","","","","","","","","","",""]
,[".soft"]
]);
new Thing("computer file",["bit,50-100"],["file"]);
new Thing("bit",[],["0","1"]);
new Thing("cute computer image",[".computer file"],[
["An image of ","A picture of ","A short video of ","A drawing of ","A slideshow of ","A video of "],
["a cat","two cats","cats","kittens","a kitten","a duckling","a duck","ducks","a puppy","a baby seal","a dog","puppies","a squid","a dolphin","a bunny","bunnies","baby bunnies","a parrot","two parrots","a gecko","a chameleon"],[" "],
["playing with a ball","befriending other animals","making cute faces","wearing silly hats","trying to play piano","in various shenanigans","playing with cardboard boxes","being really excited","sneezing","sleeping","waking up","falling asleep"],["."]
]);
new Thing("stupid computer image",[".computer file"],[
["An image of ","A picture of ","An album of ","A short video of ","A video of ","A compilation of "],
["some dude","some girl","a rather unattractive fellow","a rather unattractive lady","a grotesque individual","a clearly drunk guy","a clearly drunk girl","a bunch of kids with popped collars","some muscular guy","a masked guy","some guy with a horse mask","cosplaying kids","orange people","midgets","a midget","a movie star","some celebrity","high school kids","children","a creepy old person","old people"],[" "],
["setting fire to some stuff","involved in a retardedly dangerous prank","trying something extremely dangerous","involved in what was probably a stupid bet","doing stupid stuff","in anatomically questionable shenanigans","getting stupidly injured","stretching the limits of stupidity","in an absurdly dangerous stunt","dancing to some cheesy music","pestering dangerous animals","doing that thing with the stuff","trying too hard to be cool"],["."]
]);
new Thing("disturbing computer image",[".computer file"],[
["An image of ","A possibly illegal image of ","A crude representation of ","A disturbing representation of ","A daring representation of ","A video of "],
["a ¤¤¤¤¤¤","a group of ¤¤¤¤¤¤","several ¤¤¤¤¤¤","a couple of ¤¤¤¤¤¤"],[" "],
["in the process of ¤¤¤¤¤¤","being ¤¤¤¤¤¤ by","trying to ¤¤¤¤¤¤ on","in a ¤¤¤¤¤¤ with","involved in ¤¤¤¤¤¤ with","holding"],[" "],
["another ¤¤¤¤¤¤","two other ¤¤¤¤¤¤","their ¤¤¤¤¤¤","inside a ¤¤¤¤¤¤'s ¤¤¤¤¤¤","a ¤¤¤¤¤¤","a strange-looking ¤¤¤¤¤¤","a bewildered ¤¤¤¤¤¤"],["."]
]);
new Thing("forum post",[".pixel paragraph"],[
["A poll about ","An irate little person ranting about ","A bunch of shut-ins arguing about ","Two people sharing their love for ","Some hipsters chatting about ","Concerned parents discussing ","An inflammatory post about ","A thoughtful comment on ","An insightful post regarding ","A troll post about ","A flame war about ","Some spam about ","A comment on ","A post about ","A discussion about ","An ongoing discussion about ","A heated argument about ","A passionate discussion about ","A single person complaining about ","A group of persons enthusiastic about "],
["politics","countries","cooking","food","favorite foods","pets","religion","religious beliefs","crime","funny videos","music","favorite bands","webcomics","comics","art","video games","movies","dating advice","relationships","favorite books","famous people","astronomy","astrophysics","science","memes","spacetime","physics","foreign countries","cats","aliens","a bunch of nonsense","a controversial book","a controversial movie","friendship","stuff people put in their pockets","computers","cute things","creepy things","stupid things","gardening","cars","crime","youth","illicit substances","knitting","sports","meditation","hobbies","whatever's trendy right now","a debated topic","superheroes","trolling","jimmies being rustled","filenames","an online universe generator"],["."]
]);
new Thing("internet browser",["nested,0.5%","website"],[["Blazewolf","Interweb Discoverer","Bismuth","Savannah","Theatre"],[".soft"]]);
new Thing("website",[["forum post,1-10","disturbing computer image,1-10","cute computer image,1-10","stupid computer image,1-10","website,1-10"],"website,1-3"],[["www."],
["one","4","9","on","live","wiki","re","net","home","neat","fat","free","cool","not","something","everything","dat","my","you","that","this","face","tv","sick","cute","creepy","me","hurr","crap","web","bizz","wrong"],
["chon","speak","news","chat","gog","ddit","bad","nasty","forum","gross","pal","friends","world","rama","search","stick","retarded","tard","ville","town","cat","cats","durr","tube","space","book","music","directory"],
[".com",".com",".com",".net",".org"]]);

//hell, might as well
new Thing("internet",["website,20"],"The Internet");
new Thing("google",[".website"]);
new Thing("wikipedia",[".website"]);
new Thing("4chan",[".website"]);
new Thing("nested",["Universe"],"www.orteil.dashnet.org/nested");
new Thing("reddit",[".website"]);
new Thing("facebook",[".website"]);
new Thing("/tg/",[".website"]);
new Thing("/b/",[".website"]);
new Thing("/v/",[".website"]);
new Thing("/x/",[".website"]);

"""