from factories.generator import ListData

from sample_data.fixtures import belt
from sample_data.fixtures import gloves
from sample_data.fixtures import jacket
from sample_data.fixtures import pants
from sample_data.fixtures.tools.outfit.scarf import scarf
from sample_data.fixtures.tools.outfit.shirt import shirt
from sample_data.fixtures import shoes
from sample_data.fixtures import skirt


class Outfit:
    storage = []

    belt_data = ListData(belt)
    gloves_data = ListData(gloves)
    jacket_data = ListData(jacket)
    pants_data = ListData(pants)
    scarf_data = ListData(scarf)
    shirt_data = ListData(shirt)
    shoes_data = ListData(shoes)
    skirt_data = ListData(skirt)

    def __init__(self):
        self.gender = "male"

        self.scarf = ""
        self.jacket = ""
        self.shirt = ""
        self.pants = ""
        self.shoes = ""
        self.gloves = ""
        self.belt = ""
        self.skirt = ""
        self.armor = []

    def clear(self):
        self.scarf = ""
        self.jacket = ""
        self.shirt = ""
        self.pants = ""
        self.shoes = ""
        self.gloves = ""
        self.belt = ""
        self.skirt = ""

    def generate(self):
        self.scarf = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.scarf_data))
        self.jacket = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.jacket_data))
        self.shirt = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.shirt_data))
        self.pants = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.pants_data))
        self.shoes = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.shoes_data))
        self.gloves = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.gloves_data))
        self.belt = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.belt_data))
        self.skirt = "https://rollforfantasy.com/images/clothing/n{}/{}".format(self.gender, next(self.skirt_data))

    def load(self, name):
        return self.storage[name]

    def save(self, name):
        self.storage[name] = self

    def image(self):
        armor = ["https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + a.id + ".png" for a in self.armor]
        return {
            'body': "https://rollforfantasy.com/images/armor/" + self.gender + "/body.png",
            'armor': armor,
            'scarf': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.scarf + ".png",
            'glove': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.gloves + ".png",
            'jacket': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.jacket + ".png",
            'shirt': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.shirt + ".png",
            'shoes': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.shoes + ".png",
            'pants': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.pants + ".png",
            'skirt': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.skirt + ".png",
            'belt': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/" + self.belt + ".png",
            'bshoes': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/b" + self.shoes + ".png",
            'bshirt': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/b" + self.shirt + ".png",
            'bjacket': "https://rollforfantasy.com/images/clothing/n" + self.gender + "/b" + self.jacket + ".png",
        }


def to_pic_click():
    """
    context.clearRect(0, 0, canvas.width, canvas.height);
    $("#canvas").css({"display": "inline"});
    $($(".armPiece").get().reverse()).each(function(){
        imgTop = $(this).css("margin-top").replace('px','');
        imgLeft = $(this).css("margin-left").replace('px','');
        imgWd = $(this).css("width").replace('px','');
        imgHt = $(this).css("height").replace('px','');

        var img = new Image();
        img.src = $(this).css("background-image").replace('url(\"','').replace('\")','');
        context.drawImage(img, imgLeft, imgTop, imgWd, imgHt);
    });
    """
