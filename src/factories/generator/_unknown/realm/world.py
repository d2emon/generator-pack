from .item import Item


GOOD_WORLD = 1
BAD_WORLD = 2


class Description(Item):
    def __str__(self):
        return "{}.".format(self.text)


class DescriptionPart1(Description):
    data = [
        "The air is thick with smoke, obstructing your vision beyond a few meters",
        "A thick fog hangs in the air and obstructs your vision beyond a few yards",
        "The air stings your eyes and skin and you cough as each breath burns your lungs",
        "Thick, dark clouds block out any light from above and cover the lands in gloomy shadows",
        "The air is dry and hot, bright light blinds you and you can feel your lungs burn with every breath",
        "The air is uncomfortable humid and hot, causing you to burst out in sweat immediately",
        "Gravity is far stronger here and you can feel its pull with every step you take. It's exhausting",
        "The first thing you see is your breath in the air, but freezing air soon chills you to your core",
        "Clouds of dust fill the air, it stings your eyes and lungs with every breath and obstructs your vision",
        "The ground is covered in small holes and marks caused by acid rains, fortunately it's not raining yet",
        "A powerful wind nearly lifts you off of the ground and rain barrages down, freezing you within minutes",
        "You're up to your knees in warm, murky water. The air is hot and humid, causing you to sweat almost "
        "immediately",
        "You find yourself in almost complete darkness, were it not for the echoes you wouldn't even know you were "
        "underground",
        "Light as a feather you gently float above the surface, hanging gently in the thick smog that fills the air",
        "With each step you take you slide forward a little more. Ice covers everything, soon it might even cover you",
        "Smoke bellows out of openings in the ground, creating a thick layer of clouds that shrouds the land in "
        "shadows",
        "The land is burning, literally. Fires wreak havoc to everything that's even remotely alive, which by now is "
        "very little",
        "The ground beneath your feet is cracked and dry and the air is hot and dusty. You can feel your skin begin to "
        "sweat and your lungs burn with each breath",
        "Rocks cover virtually every surface you can see, which makes traversing this landscape tricky and dangerous",

        "Lightning strikes close to you and then again and again. The sky roars as an eternal thunder storm dominates "
        "this realm",
        "A lush landscape full of color meets your eyes. The air is warm and humid, but pleasantly so",
        "You gently float above the surface, gravity is not strong here at all. The landscape too tries to reach for "
        "the sky",
        "Snowflakes gently glide by, they cover the entire landscape in a thick layer of snow and a silence has taken "
        "hold of the air",
        "A luminous world meets your eyes. Everything's glowing in some shape or form, the animals, the plants, even "
        "some of the rocks",
        "The first thing you notice is a barrage of scents. Pleasant and calming, this world of scents is unlike any "
        "other",
        "You can hear water, lots and lots of water. Rivers roar and waterfalls tumble down towering mountain sides",
        "Lush flower petals drift down the wind and the sounds of unseen animals fills the air",
        "A dark world meets you, but as your eyes adjust you begin to see a world of bio-luminescence. Animals and "
        "plants glowing in the dark",
        "A gentle breeze caresses your face as the rays of a blueish sun warm your skin. It's occasionally blocked by "
        "a floating island, drifting by",
        "The light of a giant moon illuminates this world and bathes the lush landscape in a blueish light",
        "You find yourself face to face with enormous statues carved out of the mountains themselves. Carvings of "
        "beings you've never seen before",
        "Waterfalls pour into the lagoon you're standing in from high above. Light from the orange sun peeks over and "
        "warms you gently",
        "A tranquil world welcomes you. Calm, warm and gentle. The lush ground is all the more enticing thanks to the "
        "stronger gravity pulling you down",
        "You feel yourself able to lift off of the ground thanks to this world's gravity. Ready to explore the many "
        "islands drifting in the sky",
        "A soothing world welcomes you. Warm air touches you gently from the lush and thick forests in front of you",
        "Wet, grassy ground squishes beneath your feet. This world is rich in life, though nothing is like anything "
        "you've seen before",
        "You find yourself atop a mountain, watching over a vast jungle-like forest full of never before seen plants. "
        "Some giant, some luminescent and some even floating in the air",
        "You look upon a vast landscape of huge mountains, many of them have waterfalls that flow down and meet in a "
        "giant river flowing gently in your direction",
        "A massive, oddly colored lake reflects the even more peculiarly colored mountains in the distance. It's "
        "peaceful and quiet here",
        "A world of lights and colors meets your eye. Thousands of flowers and other lifeforms seem to glow in the "
        "greenish sun of this world"
    ]

    @property
    def world_type(self):
        if self.item_id < 19:
            return BAD_WORLD
        return GOOD_WORLD

    @classmethod
    def choice(cls, data=None, world=None, **kwargs):
        if data is None:
            data = cls.data

        if world is not None:
            if world.world_type == BAD_WORLD:
                data = data[:19]
            else:
                data = data[19:]

        return super().choice(data, **kwargs)


class DescriptionPart2(Description):
    data = [
        "A foul smell fills your nostrils, and you immediately begin to feel nauseous",
        "It's certainly not a pleasant world to live in, though some beings seem to manage",
        "The terrain's treacherous to walk on. Who knows what dangers await to those who fall",
        "A world of potential awaits, but in this case it seems like a potential for danger and death",
        "Who knows how long you could last in this world, probably not for long",
        "A strange energy hangs in the air and makes the hairs on your arms rise",
        "Low, ominous sounds can be heard in the distance or at least you hope it's in the distance",
        "Shrieks and yelps are heard all around you, but it's impossible to find their sources",
        "The sound of thick bubbles escaping some form of mud or viscous liquid can be heard all around you",
        "You could've sworn something touched your leg just now, perhaps to inspect you or to get a taste",
        "Uncertainty surrounds you and it's not the thrilling uncertainty of exploration, but a dreadful fear",
        "You feel watched even though you can't see anything watching you",
        "The light plays tricks on your eyes as shadows from a new landscape make your imagination go wild",
        "Something in the air is altering your mind, but at least it makes this world seem more pleasant",
        "It's hard to take everything in in such a harsh environment, but there's so much to see",
        "Yet there's something strangely beautiful about this isolated world of dismay",
        "Strange sounds erupt from behind you, perhaps two beings fighting each other or a collapsing landscape",
        "Your immediate instinct is to seek shelter, to find some form of relief from this atmosphere",
        "You feel nauseous, there must be something in the air, but who knows what it is",
        "Each step you take is a burden on your very being, this world is clearly not meant for you",
        "A wave of nostalgia hits you, somehow you feel at home in this strange world",
        "Any fears you had before you entered the portal are now washed away by this tranquil world",
        "A sense of calm takes over as you take in the gorgeous sights before your very eyes",
        "A sense of adventure take hold of you. This world is rich with opportunities",
        "Immediately your mind begins to wonder what's behind that hill or what lives atop that twisty tree",
        "You can't help but wonder who or what inhabits this world and you can't wait to find out",
        "You feel free, free to explore what lives in that river, what hides in that cave or where that forest ends",
        "This world erupts with life as sounds of all sorts of beings or perhaps the land itself fills the air",
        "Life here looks nothing like what you're used to. Different colors, different scents, but all very pleasing",
        "A new world has literally opened up to you, vast expanses of new life ready to be explored. You can't wait",
        "A barrage of the senses takes over as you begin to take in every element of this world you can",
        "This world seems to calm. Whether this is true or just appearances remains to be seen, but for now you're "
        "hopeful",
        "This world is different from your own, incredibly different. But despite the differences it feels familiar",
        "A sense of relief takes over as you realize this world might be safe to venture into further",
        "You know it's only been a short while, but this world feels very promising. Pleasant and seemingly "
        "non-hostile",
        "It's still best to tread cautiously, it is a new world after all, but so far so good",
        "A sense of calm takes hold of you. Perhaps this world is what you were looking for or maybe something in the "
        "air is affecting your mind",
        "You have to keep reminding yourself to not let this astonishing world lull you into a false sense of security",
        "It's a world beyond anything you had imagined. There's beauty in every corner, calm in every moment",
        "You wonder if you can trust your senses, surely a world couldn't be as seemingly pleasant as this one"
    ]


class World(Item):
    data = [
        "a depressing", "a disconcerting", "a disturbing", "a foreboding", "a frightening", "a gloomy", "a hostile",
        "a most upsetting", "a sinister", "a taxing", "a vexing", "a worrisome", "an alarming", "an inhospitable",
        "an ominous", "a bustling", "a captivating", "a charming", "a dynamic", "a fascinating", "a marvelous",
        "a pleasant", "a surprising", "a vibrant", "a vigorous", "a vivid", "a wonderful", "an enchanting",
        "an energetic", "an engaging"
    ]

    def __init__(self, item_id, text, descriptions=()):
        super().__init__(item_id, text)

        self.description = []

        if len(descriptions) < 1:
            self.description.append(DescriptionPart1.choice(world=self))
        else:
            self.description.append(descriptions[0])

        if len(descriptions) < 2:
            self.description.append(DescriptionPart2.choice())
        else:
            self.description.append(descriptions[1])

    @property
    def world_type(self):
        if self.item_id < 15:
            return BAD_WORLD
        return GOOD_WORLD

    def __str__(self):
        return "{} world".format(self.text)
