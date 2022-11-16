"""
var nm2 = ["land", "world", "zone", "park", "town", "fair", "realm", "ville", "land", "park", "ventures"];
var nm4 = ["World", "Land", "Zone", "Park", "Town", "Village", "Realm", "Fair", "Island", "Fun Park", "Fun World", "Kingdom", "Dome", "Paradise", "Experience"];
var nm7 = ["fête", "foire", "polis", "monde", "ville", "zone", "polis", "monde"];
var nm8 = ["l'Île", "l'Aventure", "la Foire", "la Terre", "la Ville", "la Zone", "le Dôme", "le Domaine", "le Monde", "le Paradis", "le Parc", "le Pays", "le Royaume", "l'Univers"];
var br = "";

var tp = type;
var nm1 = ["Angel", "Animal", "Aqua", "Arcane", "Astral", "Astro", "Aura", "Beach", "Beast", "Carny", "Cartoon", "Child", "Clown", "Comic", "Creep", "Critter", "Crypt", "Demon", "Dino", "Doll", "Dragon", "Dread", "Dream", "Elf", "Ember", "Epic", "Eterni", "Ever", "Expo", "Fable", "Fairy", "Feral", "Festi", "Film", "Fire", "Forest", "Freak", "Fright", "Fun", "Game", "Ghost", "Giant", "Groovy", "Happy", "Hell", "Hero", "Horror", "Ice", "Jungle", "Kids", "Luna", "Lunar", "Magic", "Marina", "Maze", "Mega", "Mini", "Miracle", "Mirror", "Monster", "Movie", "Mutant", "Never", "Night", "Ocean", "Paradox", "Phantom", "Play", "Quest", "Rain", "Rainbow", "River", "Robot", "Saga", "Sand", "Scream", "Secret", "Shadow", "Shock", "Sky", "Snow", "Solar", "Space", "Speed", "Spirit", "Splash", "Star", "Stellar", "Storm", "Story", "Summer", "Sun", "Super", "Terra", "Terror", "Thrill", "Titan", "Toy", "Undead", "Vision", "Warp", "Water", "Winter", "Witch", "Wizard", "Wonder", "Zombie", "Zoo"];
var nm3 = ["Adventure", "Amazing", "Amazon", "Angel", "Animal", "Animation", "Anime", "Aqua", "Arcane", "Astral", "Beach", "Beast", "Bird", "Candy", "Cartoon", "Castle", "Child", "Chocolate", "Clown", "Comic", "Creep", "Critter", "Crypt", "Crystal", "Demon", "Dino", "Dinosaur", "Discovery", "Doll", "Dragon", "Dread", "Dream", "Elf", "Ember", "Enchanted", "Epic", "Fable", "Fairy", "Fairy Tale", "Family", "Fantasy", "Feral", "Festival", "Film", "Fire", "Forest", "Freak", "Fright", "Fun", "Galaxy", "Game", "Ghost", "Giant", "Happy", "Hell", "Hero", "Horror", "Ice", "Jungle", "Kids", "King's", "Knight", "Legend", "Luna", "Lunar", "Magic", "Magic Forest", "Marina", "Marine", "Maze", "Mega", "Midnight", "Mini", "Miniature", "Miracle", "Mirror", "Monster", "Movie", "Mutant", "Mystery", "Mystic", "Mythic", "Nature", "Night", "Nightmare", "Oasis", "Ocean", "Panorama", "Paradox", "Parody", "Phantom", "Phoenix", "Pirate", "Play", "Power", "Quest", "Rain", "Rainbow", "River", "Robot", "Saga", "Sand", "Santa's", "Science", "Scream", "Secret", "Serpent", "Shadow", "Shock", "Sky", "Snow", "Solar", "Space", "Speed", "Spirit", "Splash", "Star", "Storebook", "Storm", "Story", "Summer", "Sun", "Super", "Surprise", "Terror", "Thrill", "Titan", "Toy", "Trampoline", "Transilvanian", "Undead", "Underwater", "Universe", "Vampire", "Vision", "Warp", "Water", "Werewolf", "Wild Water", "Wild West", "Wildlife", "Winter", "Witch", "Wizard", "Wonder", "Zombie", "Zoo"];
var nm5 = ["Écla", "Été", "Éterni", "Étoi", "Angeli", "Animé", "Anima", "Aqua", "Astra", "Astro", "Aura", "Automa", "Bestio", "Bouffo", "Caché", "Capri", "Carna", "Carnava", "Cauchema", "Ciné", "Comi", "Cri", "Démo", "Démon", "Diable", "Dino", "Drago", "Dragon", "Effra", "Enchanto", "Enfer", "Espri", "Expo", "Fée", "Féeri", "Fantô", "Festi", "Forê", "Frisso", "Géni", "Gami", "Glaço", "Glace", "Héroï", "Héro", "Histoi", "Horreur", "Imagi", "Jeu", "Joue", "Joyeu", "Labyri", "Labyrinto", "Lunai", "Luti", "Lutin", "Méga", "Magi", "Marino", "Mervei", "Mini", "Minui", "Mira", "Miroi", "Monstre", "Monstro", "Mutan", "Mysti", "Océa", "Ombra", "Ombre", "Ouraga", "Peti", "Plaisanti", "Prodi", "Quête", "Quêto", "Réjouissa", "Rêve", "Rêveri", "Rapi", "Rigola", "Riva", "Rivi", "Robo", "Saga", "Sensa", "Sensatio", "Sini", "Solai", "Solei", "Sorcello", "Sorci", "Stella", "Super", "Surpri", "Terra", "Tita", "Zombi", "Zoo"];
var nm6 = ["Épique", "Ésotérique", "Comique", "Drôle", "Fantôme", "Héroïque", "Imaginaire", "Incroyable", "Lunaire", "Magique", "Mythique", "Sauvage", "Solaire", "Transilvanien", "d'Éclaboussures", "d'Été", "d'Amazone", "d'Anges", "d'Animés", "d'Animation", "d'Animaux", "d'Arcs-en-Ciel", "d'Aventure", "d'Eau", "d'Eau Sauvage", "d'Elfes", "d'Enfer", "d'Espace", "d'Esprit", "d'Esprits", "d'Histoires", "d'Horreur", "d'Imagination", "d'Océan", "d'Oiseaux", "d'Ombres", "d'Orage", "d'Univers", "de Bêtes", "de Bestioles", "de Bonbons", "de Bouffons", "de Braise", "de Cauchemars", "de Châteaux", "de Chocolat", "de Courage", "de Crainte", "de Cristaux", "de Découverte", "de Découvertes", "de Démons", "de Diamants", "de Dinosaures", "de Dragons", "de Fées", "de Fêtes", "de Fables", "de Famille", "de Fantômes", "de Fantaisie", "de Faune", "de Feu", "de Frayeur", "de Frissons", "de Géants", "de Galaxie", "de Glace", "de Jeux", "de Jouets", "de Légende", "de Légendes", "de Loups-Garous", "de Magie", "de Merveille", "de Minuit", "de Miracle", "de Miroirs", "de Monstres", "de Mort-Vivant", "de Mutants", "de Mystère", "de Mystères", "de Nature", "de Neige", "de Nuit", "de Père Noël", "de Panoramas", "de Paradoxes", "de Parodie", "de Peur", "de Plage", "de Plaisanterie", "de Pluie", "de Poupées", "de Puissance", "de Quêtes", "de Rêveries", "de Rêves", "de Rigolade", "de Rire", "de Rivières", "de Robots", "de Sable", "de Sagas", "de Savoir", "de Science", "de Secrets", "de Sensations", "de Serpents", "de Soleil", "de Spectres", "de Surprise", "de Tempête", "de Trampoline", "de Vampires", "de Vitesse", "de Zombis", "de l'Oasis", "de la Crypte", "de la Forêt", "de la Forêt Magique", "de la Galaxie", "de la Jungle", "de la Légende", "de la Lune", "de la Nuit", "de la Plage", "de la Rivière", "de la Sorcière", "des Étoiles", "des Contes de Fées", "des Corsaires", "des Enfants", "des Films", "des Gamins", "des Héros", "des Miniatures", "des Miracles", "des Monstres", "des Pirates", "des Surprises", "des Titans", "du Château", "du Ciel", "du Dragon", "du Labyrinthe", "du Phénix", "du Roi", "du Soleil", "du Sorcier", "du Zoo"];


# English: tp == 0
if i < 5:
    rnd = Math.random() * nm1.length | 0;
    rnd2 = Math.random() * nm2.length | 0;
    names = nm1[rnd] + nm2[rnd2];
else:
    rnd = Math.random() * nm3.length | 0;
    rnd2 = Math.random() * nm4.length | 0;
    names = nm3[rnd] + " " + nm4[rnd2];


# French: tp == 1
if i < 5:
    rnd = Math.random() * nm5.length | 0;
    rnd2 = Math.random() * nm7.length | 0;
    names = nm5[rnd] + nm7[rnd2];
else:
    rnd = Math.random() * nm8.length | 0;
    rnd2 = Math.random() * nm6.length | 0;
    names = nm8[rnd] + " " + nm6[rnd2];
"""

from data.fng.names.place.amusement_park import first1, first2, second1, second2
from genesys.fng.database import Database
from factories.list_factory import ListFactory
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.name import Name


DB = Database('amusement-park', {
    'first1': first1,
    'first2': first2,
    'last1': second1,
    'last2': second2,
})


class AmusementPark(Name):
    def __init__(self, first="", last="", method=1):
        super().__init__()
        self.first = first
        self.last = last
        self.method = method

        
    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        if self.method == 2:
            return f"{self.first} {self.last}"

        return f"{self.first}{self.last}"


class AmusementParkFactory1(ComplexFactory):

    block_map = {
        'first': 'first1',
        'last': 'last1',
    }

    model = AmusementPark

    static_kwargs = {
        'method': 1,
    }

    def __str__(self):
        return "{}{}".format(self.first, self.last)


class AmusementParkFactory2(ComplexFactory):

    block_map = {
        'first': 'first2',
        'last': 'last2',
    }

    model = AmusementPark

    static_kwargs = {
        'method': 2,
    }


class AmusementParkFactory(MultipleFactoryNameFactory):
    default_data = DB
    factory_classes = [
        AmusementParkFactory1,
        AmusementParkFactory2,
    ]
    model = AmusementPark
