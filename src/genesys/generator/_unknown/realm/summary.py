from .item import Item


class Description(Item):
    data = [
        ", but for now you should be able to handle it", ", but there are no direct threats you have to deal with",
        ", but it's a danger you can handle", ", but at the very least you should be able to survive for a week",
        ", but if you're cautious it should be manageable", ", but with so much to discover you can't help but explore",
        ", but with great risks come great rewards", ", but even so you still fancy your chances in this world",
        ", but you reckon you'll be fine as long as you're cautious",
        ", so all you need is a healthy dose of caution and you should be fine",
        ", you should be perfectly safe as long as you use common sense",
        ", as long as you avoid accidents your journey should be amazing",
        " and the only real obstructions are your own abilities",
        " and there's nothing that could ruin this experience",
        ", with an optimistic sense of curiosity and a healthy dose of common sense you'll be good to go",
        ", but looks can be deceiving at times",
        ", but your own world has plenty of pitfalls, there's no reason this one won't either",
        ", but now is not the moment to throw caution in the wind",
        ", but you've caught but a glimpse of what this world has to offer", ", but time will tell how true this is",
    ]


class Summary(Item):
    data = [
        "definitely inhospitable", "no picnic", "no walk in the park", "no easy undertaking", "undeniably hostile",
        "certainly unwelcoming", "indubitably threatening", "precarious beyond a doubt", "clearly treacherous",
        "unmistakably menacing", "definitely gentle", "undeniably pleasant", "certainly benign", "indubitably pleasing",
        "clearly manageable", "peaceful beyond a doubt", "kind to you for sure", "smooth sailing all across",
        "an easy undertaking", "a paradise"
    ]

    def __init__(self, item_id, text, description=None):
        super().__init__(item_id, text)

        self.description = []
        if description is None:
            self.description = Description.choice()
        else:
            self.description = description

    def __str__(self):
        return "This world is {}{}.".format(self.text, self.description)
