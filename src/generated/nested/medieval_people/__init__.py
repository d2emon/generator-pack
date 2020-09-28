"""
//medieval people
new Thing("medieval clothing set",["medieval hat,30%","medieval pants,98%","medieval shirt,98%","medieval coat,50%","medieval shoes,80%","medieval underwear,99%"],"clothing");
new Thing("medieval man",[".medieval person"],"*MEDIEVAL MAN*");
new Thing("medieval woman",[".medieval person"],"*MEDIEVAL WOMAN*");
new Thing("medieval person",["body","medieval psyche","medieval clothing set"],"*MEDIEVAL PERSON*");

new Thing("medieval psyche",["medieval thoughts","medieval memories"],"psyche");
new Thing("medieval thoughts",["BlackHole,0.01%",["medieval thought,2-3"]],"thoughts");
new Thing("medieval thought",[],["*MEDIEVAL THOUGHT*"]);
new Thing("medieval memories",["medieval memory,2-4"],"memories");
new Thing("medieval memory",[],["*MEDIEVAL MEMORY*"]);

new Thing("medieval clothing",[["leather","cloth"]],["clothing"]);
new Thing("medieval pants",[".medieval clothing"],["pants"]);
new Thing("medieval shirt",[".medieval clothing"],["shirt"]);
new Thing("medieval underwear",[".medieval clothing"],["underwear"]);
new Thing("medieval coat",[".medieval clothing"],["coat","cloak","cape","robe","mantle"]);
new Thing("medieval shoes",["leather,50%","wood"],["shoes","clogs"]);
new Thing("medieval hat",[".medieval clothing"],["hat","hood","headdress"]);
new Thing("armor",["metal"],["chain-mail armor","plate armor","lamellar armor","scale armor","brigandine","cuirass","gauntlets","pauldrons","spaulders","vambraces","greaves"]);
new Thing("helmet",["metal"],["helm","helmet"]);
new Thing("medieval weapon",["metal","wood"],["sword","longsword","rapier","bow","shortbow","longbow","crossbow","mace","spear","dagger","pole axe","knife","halberd","axe","javelin","hatchet","battleaxe","warhammer","maul","staff","harpoon","scimitar","cleaver","morningstar","club"]);

new Thing("medieval peasant",[".medieval person"],"*MEDIEVAL PERSON*| (peasant)");
new Thing("medieval priest",[".medieval person"],"*MEDIEVAL PERSON*| (priest)");
new Thing("medieval servant",[".medieval person"],"*MEDIEVAL PERSON*| (servant)");
new Thing("medieval noble",[".medieval person"],"*MEDIEVAL PERSON*| (noble)");
new Thing("medieval guard",[".medieval person"],"*MEDIEVAL PERSON*| (guard)");
new Thing("medieval shopkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (shopkeeper)");
new Thing("medieval innkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (innkeeper)");
new Thing("medieval king",[".medieval person"],[["*MEDIEVAL MAN*| ("],["king","emperor","prince"],[")"]]);
new Thing("medieval queen",[".medieval person"],[["*MEDIEVAL WOMAN*| ("],["queen","empress","princess"],[")"]]);
new Thing("wizard",[".medieval person"],[["*MEDIEVAL PERSON*| ("],["court","battle","rogue","corrupt","druid","bard","adept","thaumaturgist","shaman","healing","ice","frost","snow","arcane","lightning","thunder","earth","earthquake","nature","animal","shape-shifting","death","undeath","spark","fire","lava","locust","poison","rainbow","mist","fog","dust","air","wind","cloud","tornado","shark","punch","kick","song","skeleton","psycho","illusion","flying","summoner","thief","barbarian","dragon","gem","sky","star","dark","paladin","luck","time","space","blade"],[" "],["mage","magician","wizard"],[")"]]);
new Thing("medieval gravedigger",[".medieval person","shovel,30%"],"*MEDIEVAL PERSON*| (gravedigger)");
new Thing("medieval corpse",["body","medieval clothing set","blood,35%","worm,20%","worm,10%"],"*MEDIEVAL PERSON*| (dead)");

"""
