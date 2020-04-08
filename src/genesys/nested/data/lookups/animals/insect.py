from genesys.nested.data.lookups.lookup import Lookup


anthill = Lookup('anthill', 'termite mound')
beehive = Lookup('beehive', 'wasp nest', 'hornet nest')
insects = Lookup(
    'ant', 'bee', 'wasp', 'hornet', 'ladybug', 'cockroach', 'termite', 'beetle', 'dung beetle', 'scarab beetle',
    'bumblebee', 'spider', 'scorpion', 'tarantula', 'praying mantis', 'butterfly', 'moth', 'fly', 'cricket',
    'mole cricket', 'cicada', 'weevil', 'stick insect', 'aphid', 'flea', 'lice', 'firefly', 'gnat', 'stinkbug',
    'grasshopper', 'silverfish', 'locust', 'earwig',
)
insect_thoughts = Lookup(
    'skitter', 'skitter skitter', 'squirm squirm', 'crawl crawl', 'buzz', 'big noisy things', 'small tasty things',
    'too much sun', 'not enough sun', 'need water', 'need food', 'need shelter', 'food please', 'mating please',
    'must defend nest', 'intruder detected', 'must spawn eggs', 'hey hey', 'let\'s be bros', 'no stomp please',
    'go away',
)
social_insects = Lookup('worker', 'soldier', 'drone')
social_insect_thoughts = Lookup(
    'hello intruder', 'you should stay away intruder',
    'intruder we may be forced to chop you up into little pieces if you stay here',
    'this is no place for you intruder', 'why don\'t you go back to your intruder nest with all the other intruders',
    'we have no need for intruders right now', 'hey intruder ever heard of personal space',
    'sorry intruder but you\'re kind of in the way', 'intruder that\'s enough now',
    'intruder why don\'t you come back another time', 'sorry intruder we\'re all super-busy here',
    'hey intruder you\'re like very big so please don\'t stay here', 'i trophallaxized a girl and i liked it',
)
