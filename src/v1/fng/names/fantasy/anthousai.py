from v1.fng.genesys.name_factory import NameFactory, GenderNameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data
from v1.fng.genesys.genders import MALE, FEMALE


nm1 = ["Acanthus", "Achillea", "Aconitum", "Aechmea", "Agapanthus", "Ageratum", "Alcea", "Alchemilla", "Allium", "Aloe",
       "Alstroemeria", "Alyssum", "Amaranthus", "Amaryllis", "Amarynth", "Amsonia", "Anemone", "Angelonia", "Anthurium",
       "Antirrhinum", "Aquilegia", "Arbutus", "Asclepias", "Aster", "Astilbe", "Astrantia", "Aubreita", "Aubretia",
       "Begonia", "Bergenia", "Bluebell", "Bouvardia", "Buddleja", "Buttercup", "Calendula", "Calla", "Calliandra",
       "Campanula", "Canna", "Cardamine", "Cardinal", "Cardinalis", "Carnation", "Celosia", "Chrysanthemum", "Cistus",
       "Clarkia", "Clematis", "Clintonia", "Clivia", "Clover", "Columbine", "Coral", "Coreopsis", "Coronaria", "Cosmos",
       "Crocosmia", "Crocus", "Cyclamen", "Daffodil", "Dahlia", "Daisy", "Daphne", "Delphiniu", "Dianella", "Dianthus",
       "Diascia", "Dicentra", "Dichondra", "Dietes", "Digitalis", "Echinacea", "Echium", "Eranthus", "Erica",
       "Erigeron", "Erysimum", "Euphoma", "Euphorbia", "Eustoma", "Flannel", "Forsythia", "Frangipani", "Freesia",
       "Fritillaria", "Fuschia", "Gaillardia", "Galanthus", "Gardenia", "Gaura", "Gazania", "Geranium", "Gerbera",
       "Gladiolus", "Gypsophila", "Heather", "Hebe", "Helenium", "Helianthi", "Helianthus", "Heliotrope", "Hellebore",
       "Hibiscus", "Holly", "Hollyhock", "Honesty", "Honeysuckle", "Hortensia", "Hosta", "Houstonia", "Hoya",
       "Hyacinth", "Hydrangea", "Hypericum", "Iberis", "Ilex", "Impatiens", "Ipheion", "Ipomea", "Ipomoea", "Iridaceae",
       "Iris", "Ixia", "Ixora", "Jaborosa", "Jamesia", "Jasmine", "Jonquil", "Kalmia", "Knautia", "Kniphofia",
       "Lantana", "Lavandula", "Lavatera", "Lavender", "Lilac", "Lilium", "Lily", "Linaria", "Lisianthus", "Lizzie",
       "Lobelia", "Lonicera", "Lotus", "Lunaria", "Lupin", "Lupinus", "Lychnis", "Magnolia", "Majalis", "Mallow",
       "Mandevilla", "Marigold", "Matthiola", "Meconopsis", "Mimosa", "Mina", "Miniata", "Monarda", "Muscari",
       "Mycositis", "Narcissus", "Nasturium", "Nasturtium", "Nelumbo", "Nemesia", "Nemophila", "Nepeta", "Nerine",
       "Nierembergia", "Nigella", "Nightshade", "Nolana", "Nucifera", "Nymphaea", "Nymphea", "Oenothera", "Orchid",
       "Pansy", "Papaver", "Passiflora", "Pelargonium", "Penstemon", "Peony", "Petunia", "Phlox", "Plumeria",
       "Pointsettia", "Polemonium", "Polyanthus", "Poppy", "Portulaca", "Primrose", "Primula", "Quince", "Rondeletia",
       "Rose", "Rosea", "Rudbeckia", "Ruellia", "Sage", "Salvia", "Saponaria", "Scabiosa", "Scaevola", "Scilla",
       "Sedum", "Silene", "Snowdrop", "Solidago", "Spraxis", "Statice", "Syriacus", "Syringa", "Tagates", "Tagetes",
       "Tanacetum", "Thunbergia", "Tigridia", "Tithonia", "Torenia", "Trachelium", "Trillium", "Triteleia", "Tritonia",
       "Trollius", "Tropaeolum", "Tuberose", "Tulip", "Tulipa", "Ursinia", "Uva", "Verbena", "Veronica", "Viburnum",
       "Vinca", "Viola", "Violet", "Watsonia", "Wedelia", "Weigela", "Wisteria", "Xylobium", "Xylosma", "Yarrow",
       "Zenobia", "Zephyranthes", "Zinnia", "Aeichloris (Leek-Green)", "Aeichloros (Leek-Green)",
       "Aithalothes (Soot-Black)", "Argyris (Silver)", "Argyros (Silver)", "Aryaeis (White)", "Aryefis (Silver-White)",
       "Aryefos (Silver-White)", "Aryennis (White)", "Aryennos (White)", "Chlois (Yellow-Green)",
       "Chloos (Yellow-Green)", "Chloromelas	(Dark Green)", "Chrysis (Gold)", "Chrysos (Gold)", "Cyanis (Blue)",
       "Cyanos (Blue)", "Earochrois (Fresh Green)", "Earochroos (Fresh Green)", "Enochris (Yellowish)",
       "Enochros (Yellowish)", "Epochris (Yellowish)", "Epochros (Yellowish)", "Erethris (Red)", "Erethros (Red)",
       "Erythis (Red)", "Erythos (Red)", "Erythris (Orange)", "Erythros (Orange)", "Eychloris (Greenish)",
       "Eychloros (Greenish)", "Eykirris (Pale Yellow)", "Eykirros (Pale Yellow)", "Falis (White)", "Falos (White)",
       "Ioeis (Dark Violet)", "Ion (Violet)", "Iothes (Verdrigris)", "Kataperis (Deep Red)", "Kataperos (Deep Red)",
       "Keanosis (Dark Blue)", "Kirris (Orange-Tawny)", "Kirros (Orange-Tawny)", "Knekis (Tawny)", "Knekos (Tawny)",
       "Koraxis (Raven Black)", "Koraxos (Raven Black)", "Leekerethris (White-Red)", "Leekerethros (White-Red)",
       "Leekochloris (Pale-Green)", "Leekochloros (Pale-Green)", "Leekoion (Violet-White)", "Leekon (White)",
       "Leekorothiis (Rose-Pink)", "Leekorothios (Rose-Pink)", "Leucis (White)", "Leucos (White)", "Melas (Black)",
       "Mesochlois (Greenish)", "Mesochloos (Greenish)", "Nifaryes (Snow White)", "Ochra (Ochre)",
       "Ochroleekis (Yellow-White)", "Ochroleekos (Yellow-White)", "Perroxanthis (Yellow-Red)",
       "Perroxanthos (Yellow-Red)", "Prasinis (Light Green)", "Prasinoeithes (Leek-Green)", "Prasinos (Light Green)",
       "Prasoeithes	(Leek-Green)", "Prasothes (Leek-Green)", "Prochloris (Greenish)", "Prochloros (Greenish)",
       "Smaraythizo	(Smaragdus Green)", "Thafoinis (Tawny)", "Thafoinos (Tawny)", "Thalassoeithes (Sea Green)",
       "Thiaperris (Bright Red)", "Thiaperros (Bright Red)", "Uperkeaneos (Very Dark Blue)", "Upochris (Pale Yellow)",
       "Upochros (Pale Yellow)", "Uthatochloris (Water-Green)", "Uthatochloros (Water-Green)",
       "Vatrachites (Frog-Green)", "Venetis (Blue)", "Venetos (Blue)", "Xanthis (Yellow)", "Xanthochros (Brown)",
       "Xantholeekis (Pale Yellow)", "Xantholeekos (Pale Yellow)", "Xanthomelinis (Yellow-Green)",
       "Xanthomelinos (Yellow-Green)", "Xanthos (Yellow)", "Yalaktinis (Milky White)", "Yalaktinos (Milky White)",
       "Yalvina (Yellow-Green)"]
nm2 = ["Aéthionéma", "Abutilon", "Acanthe", "Achillée", "Aconit", "Adénostyles", "Adonis", "Aeonium", "Aigremoine",
       "Airelle", "Ajonc", "Alchemilla", "Alchemille", "Alliaire", "Allium", "Aloë", "Aloe", "Alyssum", "Amélanchier",
       "Amaryllis", "Amourette", "Anémone", "Ancolie", "Androsace", "Andryala", "Andryale", "Anemone", "Angélique",
       "Angelica", "Antennaria", "Anthémis", "Anthillide", "Anthrisque", "Anthyllis", "Aphyllante", "Aphyllanthes",
       "Aptenia", "Aquilegia", "Arabette", "Arenaria", "Arisarum", "Aristoloche", "Aristolochia", "Arméria", "Arnica",
       "Arnoséris", "Arum", "Asarina", "Asarine", "Aspérule", "Asperge", "Asperula", "Asphodèle", "Asplénium",
       "Astérolide", "Aster", "Astragale", "Astrance", "Astrantia", "Bérardie", "Badasse", "Ballota", "Ballote",
       "Balsamine", "Barbarée", "Barbarea", "Bartsia", "Bartsie", "Belladone", "Benoîte", "Berardia", "Berce",
       "Biserrula", "Botryche", "Brunelle", "Bruyère", "Buglosse", "Bugrane", "Buphtalme", "Busserole", "Céraiste",
       "Calament", "Calendula", "Calluna", "Callune", "Camérisier", "Campanula", "Campanule", "Capparis", "Capucine",
       "Cardère", "Cardamine", "Carillon", "Carlina", "Carline", "Carraluma", "Centaurée", "Centaurea", "Cerastium",
       "Chélidoine", "Chenillette", "Chicorée", "Chrysanthème", "Circée", "Circaea", "Cirse", "Cirsium", "Clématite",
       "Colchique", "Colza", "Consolida", "Coris", "Coronilla", "Coronille", "Corydale", "Cosentinia", "Courroie",
       "Crépide", "Crepis", "Cruciata", "Cyclamen", "Cytinet", "Cytise", "Dactyle", "Daphné", "Daphne", "Dauphinelle",
       "Dianthus", "Dorine", "Droséra", "Edelweiss", "Epervière", "Epiaire", "Epilobe", "Epipactis", "Erine", "Erodium",
       "Euphorbe", "Euphorbia", "Euphraise", "Euphrasia", "Férule", "Ficoïde", "Fragaria", "Fumaria", "Fumeterre",
       "Gagée", "Gaillet", "Galéoptis", "Galatella", "Galium", "Genista", "Genoite", "Gentiane", "Geranium",
       "Germandrée", "Gesse", "Gessette", "Glaïeul", "Glaucière", "Glaucium", "Glebionis", "Grémil", "Gymnadenia",
       "Hélianthème", "Hépatique", "Hellébore", "Helleborus", "Horminelle", "Hutchinsia", "Ibéris", "Iberis", "Inule",
       "Iris", "Jacinthe", "Jasione", "Jasmin", "Jonquille", "Laiteron", "Laitue", "Lamier", "Lamium", "Lathrée",
       "Lathyrus", "Launée", "Lavande", "Lila", "Limodore", "Limonium", "Lin", "Linaire", "Linaria", "Lis", "Liseron",
       "Listère", "Lonicera", "Lotier", "Lotus", "Luzerne", "Luzule", "Lychnis", "Lycium", "Mélampyre", "Mélilot",
       "Mélitte", "Mahonia", "Malva", "Marguerite", "Massette", "Matricaire", "Matthiola", "Mauve", "Mentha", "Menthe",
       "Mimule", "Misopate", "Molène", "Moricandia", "Moricandie", "Mouron", "Muflier", "Muscari", "Myosotis",
       "Myrtille", "Nénuphar", "Néotine", "Néottie", "Narcisse", "Neotinea", "Neottia", "Nigritelle", "Nombril",
       "Nonea", "Notoceras", "Odontite", "Oeillet", "Onagre", "Ononis", "Onosma", "Ophrys", "Orcanette", "Orchidée",
       "Orchis", "Origan", "Ornithogale", "Orobanche", "Orpin", "Ortie", "Oseille", "Oxalis", "Pallénis", "Parnassia",
       "Parnassie", "Passerage", "Pensée", "Phalangère", "Phlomis", "Phyteuma", "Picride", "Pigamon", "Pilosella",
       "Pivoine", "Potentille", "Prèle", "Primevère", "Primula", "Pulicaria", "Pulsatilla", "Pulsatille", "Pyrola",
       "Pyrole", "Réséda", "Ramonda", "Ramonde", "Renoncule", "Reseda", "Rhinanthe", "Ronce", "Rosa", "Rose", "Séséli",
       "Sabline", "Sabot", "Sagine", "Salsifis", "Salsola", "Salvia", "Sauge", "Scilla", "Scille", "Sedum", "Silène",
       "Silene", "Sisymbre", "Sonchus", "Succise", "Tanaisie", "Teucrium", "Thalictrum", "Thym", "Trèfle", "Tulipe",
       "Urtica", "Véronique", "Valériane", "Valeriana", "Verveine", "Vicia", "Viola", "Violette", "Vipérine",
       "Withaine", "Aeichloris (Leek-Green)", "Aeichloros (Leek-Green)", "Aithalothes (Soot-Black)", "Argyris (Silver)",
       "Argyros (Silver)", "Aryaeis (White)", "Aryefis (Silver-White)", "Aryefos (Silver-White)", "Aryennis (White)",
       "Aryennos (White)", "Chlois (Yellow-Green)", "Chloos (Yellow-Green)", "Chloromelas	(Dark Green)",
       "Chrysis (Gold)", "Chrysos (Gold)", "Cyanis (Blue)", "Cyanos (Blue)", "Earochrois (Fresh Green)",
       "Earochroos (Fresh Green)", "Enochris (Yellowish)", "Enochros (Yellowish)", "Epochris (Yellowish)",
       "Epochros (Yellowish)", "Erethris (Red)", "Erethros (Red)", "Erythis (Red)", "Erythos (Red)",
       "Erythris (Orange)", "Erythros (Orange)", "Eychloris (Greenish)", "Eychloros (Greenish)",
       "Eykirris (Pale Yellow)", "Eykirros (Pale Yellow)", "Falis (White)", "Falos (White)", "Ioeis (Dark Violet)",
       "Ion (Violet)", "Iothes (Verdrigris)", "Kataperis (Deep Red)", "Kataperos (Deep Red)", "Keanosis (Dark Blue)",
       "Kirris (Orange-Tawny)", "Kirros (Orange-Tawny)", "Knekis (Tawny)", "Knekos (Tawny)", "Koraxis (Raven Black)",
       "Koraxos (Raven Black)", "Leekerethris (White-Red)", "Leekerethros (White-Red)", "Leekochloris (Pale-Green)",
       "Leekochloros (Pale-Green)", "Leekoion (Violet-White)", "Leekon (White)", "Leekorothiis (Rose-Pink)",
       "Leekorothios (Rose-Pink)", "Leucis (White)", "Leucos (White)", "Melas (Black)", "Mesochlois (Greenish)",
       "Mesochloos (Greenish)", "Nifaryes (Snow White)", "Ochra (Ochre)", "Ochroleekis (Yellow-White)",
       "Ochroleekos (Yellow-White)", "Perroxanthis (Yellow-Red)", "Perroxanthos (Yellow-Red)", "Prasinis (Light Green)",
       "Prasinoeithes (Leek-Green)", "Prasinos (Light Green)", "Prasoeithes	(Leek-Green)", "Prasothes (Leek-Green)",
       "Prochloris (Greenish)", "Prochloros (Greenish)", "Smaraythizo	(Smaragdus Green)", "Thafoinis (Tawny)",
       "Thafoinos (Tawny)", "Thalassoeithes (Sea Green)", "Thiaperris (Bright Red)", "Thiaperros (Bright Red)",
       "Uperkeaneos (Very Dark Blue)", "Upochris (Pale Yellow)", "Upochros (Pale Yellow)",
       "Uthatochloris (Water-Green)", "Uthatochloros (Water-Green)", "Vatrachites (Frog-Green)", "Venetis (Blue)",
       "Venetos (Blue)", "Xanthis (Yellow)", "Xanthochros (Brown)", "Xantholeekis (Pale Yellow)",
       "Xantholeekos (Pale Yellow)", "Xanthomelinis (Yellow-Green)", "Xanthomelinos (Yellow-Green)", "Xanthos (Yellow)",
       "Yalaktinis (Milky White)", "Yalaktinos (Milky White)", "Yalvina (Yellow-Green)"]


# Models


class AnthousaiName(Name):
    @property
    def value(self):
        return f"{self.items[1]}"


# Factory

class AnthousaiNameFactory(GenderNameFactory):
    """Anthousai Name Factory"""

    class MaleAnthousaiNameFactory(NameFactory):
        name_class = AnthousaiName
        blocks_map = {
            1: 1,
        }

    class FemaleAnthousaiNameFactory(NameFactory):
        name_class = AnthousaiName
        blocks_map = {
            1: 2,
        }

    description = """Anthousai are flower nymphs, just as dryads are tree nymphs. But unlike dryads, anthousai aren't
        as well known outside of Greek mythology.
        Anthousai have hair that resembles hyacinths, a plant with flowers in vibrant colors ranging from white to blues
        to purples. Being nymphs, they're usually associated with female freedom and sexuality, but the extend of this
        can vary from simply free, female deities of nature to sexually promiscuous deities out to seduce men.

        Known anthousai names range are usually either color names or flower names, but we usually named flowers after
        Greek deities rather than the other way round. This name generator has both flower names and color names, but
        the flower names are mostly in Latin (as well as English or French depending on your choice below). Colors have
        their translation in brackets. Gender doesn't seem to matter for names, as Chloris is spelled with the masculine
        suffix despite being a woman."""
    factory_classes = {
        MALE: MaleAnthousaiNameFactory,
        FEMALE: FemaleAnthousaiNameFactory,
    }
    default_blocks = load_data({
        1: nm1,
        2: nm2,
    })
