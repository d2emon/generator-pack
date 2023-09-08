from factories.list_factory import ListFactory
from genesys.fng.factories.description.character import Male, Female
from genesys.fng.factories import SleeveLength


class DataProvider:
    class TieDataProvider:
        @property
        def descriptions(self):
            return ListFactory([
                "tightly tied with string",
                "loosely tied with string",
                "buttoned up completely",
                "almost completely buttoned up",
                "half buttoned up",
                "barely tied with string",
                "barely buttoned up",
                "bound",
            ])

        @property
        def positions(self):
            return ListFactory([
                "at the center",
                "at the left side",
                "at the right side",
                "at the top left side",
                "at the top right side",
                "at the bottom left side",
                "at the bottom right side",
                "slightly off-center",
            ])

    class SleeveDataProvider:
        @property
        def lengths(self):
            return ListFactory([
                SleeveLength("long", True),
                SleeveLength("very long", True),
                SleeveLength("fairly long", True),
                SleeveLength("short"),
                SleeveLength("very short"),
                SleeveLength("fairly short"),
            ])

        @property
        def widths(self):
            return ListFactory([
                "incredibly wide",
                "very wide",
                "quite wide",
                "wide",
                "a little wide",
                "narrow",
                "quite narrow",
                "a little narrow",
                "a comfortable fit",
                "a loose fit",
            ])

        @property
        def reachs(self):
            return ListFactory([
                "his hands",
                "just above his hands",
                "well below his hands",
                "below his hands",
                "well above his hands",
                "his wrists",
                "just below his wrists",
                "just above his wrists",
                "well above his wrists",
                "well below his wrists",
            ])

        @property
        def decorations(self):
            return ListFactory([
                "a single thread lining from top to bottom",
                "several thread linings from top to bottom",
                "a single thread lining at the sleeve ends",
                "several thread linings at the sleeve ends",
                "a decorative band at the edges",
                "a decorative band almost at the edges",
                "a single thread lining and a decorative band",
            ])

    class DressSleeveDataProvider(SleeveDataProvider):
        @property
        def lengths(self):
            return ListFactory([
                SleeveLength("very long", True),
                SleeveLength("quite long", True),
                SleeveLength("a little too long", True),
                SleeveLength("purposely too long", True),
                SleeveLength("incredibly long", True),
                SleeveLength("the length of her arms", True),
                SleeveLength("longer than her arms", True),
                SleeveLength("slightly shorter than her arms", True),
                SleeveLength("almost the length of her arms", True),
                SleeveLength("fairly short"),
                SleeveLength("a little short"),
            ])

        @property
        def widths(self):
            return ListFactory([
                "incredibly wide",
                "very wide",
                "quite wide",
                "wide",
                "a little wide",
                "narrow",
                "quite narrow",
                "a little narrow",
                "a comfortable fit",
                "a loose fit",
            ])

        @property
        def reachs(self):
            return ListFactory([
                "his hands",
                "just above his hands",
                "well below his hands",
                "below his hands",
                "well above his hands",
                "his wrists",
                "just below his wrists",
                "just above his wrists",
                "well above his wrists",
                "well below his wrists",
            ])

        @property
        def decorations(self):
            return ListFactory([
                "a single thread lining from top to bottom",
                "several thread linings from top to bottom",
                "a single thread lining at the sleeve ends",
                "several thread linings at the sleeve ends",
                "a decorative band at the edges",
                "a decorative band almost at the edges",
                "a single thread lining and a decorative band",
            ])

        @property
        def change_positions(self):
            return ListFactory([
                "just below the shoulder",
                "just below the elbow",
                "just above the elbow",
                "below the shoulder",
                "below the elbow",
                "above the elbow",
                "well below the shoulder",
                "well below the elbow",
                "well above the elbow",
                "at the elbow",
                "at the shoulder",
            ])

        @property
        def change_types(self):
            return ListFactory([
                "they change color and where ",
                "",
            ])

    class MaterialDataProvider:
        @property
        def materials(self):
            return ListFactory([
                ("leather",),
                ("hide",),
                ("furred",),
                ("leather", "soft leather"),
                ("leather", "hard leather"),
                ("cloth", "bound cloth"),
            ])

        @property
        def rarities(self):
            return ListFactory([
                "rare",
                "very rare",
                "fairly rare",
                "fairly uncommon",
                "very uncommon",
                "pretty uncommon",
                "pretty rare",
                "pretty unusual",
                "pretty unique",
            ])

    class ShirtDataProvider:
        @property
        def styles(self):
            return ListFactory([
                "rough",
                "elegant",
                "fancy",
                "graceful",
                "luxurious",
                "relatively simple",
                "majestic",
                "modest",
                "noble",
                "ornate",
                "rather simple",
                "refined",
                "stylish",
                "traditional",
            ])

    @property
    def genders(self):
        return ListFactory([
            Male,
            Female,
        ])
