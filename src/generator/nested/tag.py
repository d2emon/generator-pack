DOM = dict()
CONTAINERS = dict()
DIVS = dict()


def get_DOM():
    global DOM
    return DOM


def add_tag(tag="div", id=None, **kwargs):
    global DOM
    if id is None:
        id = len(DOM)
    tag_data ={
        "tag": tag,
        "id": id,
        "props": kwargs
    }
    DOM[id] = tag_data
    return tag_data

def add_container(id, **kwargs):
    global CONTAINERS
    t = add_tag(
        id="container{}".format(id),
        **kwargs
    )
    CONTAINERS[id] = t
    return t

def add_div(id, **kwargs):
    global DIVS
    t = add_tag(
        id="div{}".format(id),
        **kwargs
    )
    DIVS[id] = t
    return t

def add_arrow(tag):
    t = add_tag(
        "a",
        href = tag.toggle,
        style = {"padding-right": "8px;"},
        alt = "archetype: {}".format(tag.archetype),
        title = "archetype: {}".format(tag.archetype),
        children = [
            add_tag(
                "span",
                id="arrow{}".format(tag.id),
                className="arrow",
                children=["+"]
            ),
            tag.name
        ]

    )
    return t


class Tag:
    def __init__(self, item):
        self.item = item

    @property
    def id(self):
        return self.item.id

    @property
    def name(self):
        return self.item.raw_name

    @property
    def archetype(self):
        return self.item.type.name

    @property
    def style(self):
        style = {"display": "none"}
        # special - case pictures
        if self.name == "sharkverse":
            style["background-image"] = "nestedSharkverse.png"
        elif self.name == "baconverse":
            style["background-image"] = "nestedBaconverse.png"
        elif self.name == "doughnutverse":
            style["background-image"] = "nestedDoughnutverse.png"
        elif self.name == "lasagnaverse":
            style["background-image"] = "nestedLasagnaverse.png"
        return style

    def children_tag(self, item):
        return add_div(
            item.id,
            children=[item.raw_name],
        )

    def text(self, *args, **kwargs):
        children = [self.children_tag(i) for i in self.item.children]

        """
        if len(self.item.children) > 0:
            div = [
                add_tag(
                    "span",
                    None,
                    onclick=self.toggle,
                    children=[
                        add_tag(
                            "span",
                            "arrow{}".format(self.id),
                            className="arrow",
                            children=["+"]
                        ),
                        self.name
                    ]
                ),
                add_container(
                    self.id,
                    className="thing",
                    style={
                        "display": "none"
                    },
                    children=children
                )

            ]
        """
        if len(self.item.children) > 0:
            return [
                add_arrow(self),
                add_container(
                    self.id,
                    className="thing",
                    style=self.style,
                    children=children,
                )

            ]
        else:
            return [
                add_tag(
                    "span",
                    className="emptyThing",
                    children=[self.name],
                )
            ]

    def toggle(self):
        global DOM
        if self.item.display == 0:
            for c in self.children:
                if not c.grown:
                    c.Grow(0)
                    Tag(c).text()

            self.item.display = 1
            DOM.get("container" + self.id)["style"]["display"] = "block"
            DOM.get("arrow" + self.id)["children"] = ["-"]
        elif self.item.display == 1:
            self.item.display = 0
            DOM.get("container" + self.id)["style"]["display"] = "none"
            DOM.get("arrow" + self.id)["children"] = ["+"]