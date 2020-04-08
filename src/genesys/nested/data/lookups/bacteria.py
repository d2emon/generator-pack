from .lookup import Lookup


bacteria_types = Lookup('amoeba', 'bacteria', 'virus')
bacteria_subtypes = Lookup(
    'pico', 'nitro', 'sulfuro', 'oxy', 'toxi', 'micro', 'nano', 'proto', 'archi', 'ferro', 'mono', 'poly', 'schizo',
    'myxo', 'hydro', 'noo', 'zoo', 'phyto', 'aqui', 'acido', 'cyano', 'chloro', 'chromo', 'fibro', 'osteo', 'spiro',
    'bacillo', 'flagello', 'helio', 'anaero', 'photo', 'litho', 'methano', 'cerebro', 'cephalo', 'brachio', 'plasmo',
    'ethylo',
)
