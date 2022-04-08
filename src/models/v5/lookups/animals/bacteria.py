from models.v5.lookups.lookup import Lookup


bacteria_types = Lookup('amoeba', 'bacteria', 'virus')
bacteria_subtypes = Lookup(
    'pico', 'nitro', 'sulfuro', 'oxy', 'toxi', 'micro', 'nano', 'proto', 'archi', 'ferro', 'mono', 'poly', 'schizo',
    'myxo', 'hydro', 'noo', 'zoo', 'phyto', 'aqui', 'acido', 'cyano', 'chloro', 'chromo', 'fibro', 'osteo', 'spiro',
    'bacillo', 'flagello', 'helio', 'anaero', 'photo', 'litho', 'methano', 'cerebro', 'cephalo', 'brachio', 'plasmo',
    'ethylo',
)
bacteria_thoughts = Lookup(
    '#wow', '#wow okay', '#i can\'t even', '#okay', '#me', '#yes', '#what', '#how', '#delicious', '#seriously',
    '#but seriously tho', '#germ life', '#mitosis', '#meiosis', '#nucleus', '#cytoplasm',
    '#single-celled and ready to mingle', '#lame', '#meh', '#i don\'t wanna talk about it', '#eukaryote privilege',
    '#protist scum', '#squirm', '#protist patriarchy', '#osmosis', '#one cell of a guy',
)
