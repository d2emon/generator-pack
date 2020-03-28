from ...provider.list_item import ListItemProvider


class DataProvider:
    tie_descriptions = [
        "tightly tied with string",
        "loosely tied with string",
        "buttoned up completely",
        "almost completely buttoned up",
        "half buttoned up",
        "barely tied with string",
        "barely buttoned up",
        "bound",
    ]
    tie_positions = [
        "at the center",
        "at the left side",
        "at the right side",
        "at the top left side",
        "at the top right side",
        "at the bottom left side",
        "at the bottom right side",
        "slightly off-center",
    ]
    jacket_materials = ListItemProvider([
        # Material("leather"),
        # Material("hide"),
        # Material("furred"),
        # Material("cloth"),
        # Material("animal skin"),
        # Material("silky"),
        # Material("velvety"),
    ])
    jacket_covers = ListItemProvider([
        "just below his waist",
        "well below his waist",
        "just below his groin",
        "well below his groin",
        "just below his knees",
        "well below his knees",
        "just above his waist",
        "well above his waist",
        "just above his groin",
        "well above his groin",
        "just above his knees",
        "well above his knees",
        "his waist",
        "his knees",
        "his groin",
    ])
    jacket_necklines = ListItemProvider([
        "round neckline",
        "wide, round neckline",
        "narrow, round neckline",
        "deep, round neckline",
        "wide v-neck",
        "narrow v-neck",
        "deep v-neck",
        "rectangular neckline",
        "wide, rectangular neckline",
        "narrow, rectangular neckline",
        "deep, rectangular neckline",
    ])
