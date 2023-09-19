"""
//war stuff
new Thing("battlefield",["soldier,10-30","corpse,10-30","blood"]);
new Thing("soldier",[".person","arsenal","blood,20%","bullet wound,0-3"],[["*PERSON*| "],["(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(officer)","(lieutenant)","(captain)","(major)"]]);
new Thing("arsenal",["gas mask,20%","rifle,90%","knife,80%","handgun,90%","handgun,50%","knife,30%","ammo pack,0-4","grenade,0-4","bullet,0-5"]);
new Thing("bullet",[
    element_factories['Cu'].one(),
    element_factories['Pb'].one(),
]);
new Thing("rifle",[
    SteelFactory.one(),
    element_factory['Al'].one().probable(50),
    PolymersFactory.probable(20),
    "bullet,0-6"]);
new Thing("handgun",[
    SteelFactory.one(),
    element_factory['Al'].one().probable(50),
    PolymersFactory.probable(20),
    "bullet,0-6"]);
new Thing("gun",[".handgun"]);
new Thing("knife",[
    SteelFactory.one(),
    "blood,10%"]);
new Thing("wound",["blood","worm,5%"],"wound");
new Thing("ammo pack",["bullet,0-20",["metal",
    PlasticFactory.one(),
]]);
new Thing("grenade",[
    IronFactory.one(),
    "TNT",["metal",
    PlasticFactory.one(),
]]);
new Thing("TNT",[
    CarbonFactory.one(),
    element_factory['H'].one(),
    element_factories['O'].one(),
    element_factories['N'].one(),
],"TNT");
new Thing("gas mask",["metal",
    PolymersFactory.one(),
    "cloth"]);
new Thing("bullet wound",["blood","worm,5%","bullet,50%","bullet,30%","bullet,10%","bullet,2%"],"wound");
"""
