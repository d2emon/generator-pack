from ..thing import Thing


class Multiverse(Thing):
    type_name = "multiverse"
    children_data = ["universe,10-30"]
    names_data = ["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"]


class Universe(Thing):
    type_name = "universe"
    children_data = ["supercluster,10-30"]


class Supercluster(Thing):
    type_name = "supercluster"
    children_data = ["galaxy,10-30"]
    names_data = "galactic supercluster"


class Galaxy(Thing):
    type_name = "galaxy"
    children_data = ["galaxy center","galaxy arm,2-6"]


class GalaxyArm(Thing):
    type_name = "galaxy arm"
    children_data = ["galactic life,5%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12","black hole,20%","black hole,20%"]
    names_data = "arm"


class GalaxyCenter(Thing):
    type_name = "galaxy center"
    children_data = ["black hole","galactic life,10%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12"]
    names_data = "galactic center"


CONTENTS = [
    Multiverse,
    Universe,
    Supercluster,
    Galaxy,
    GalaxyArm,
    GalaxyCenter,
]