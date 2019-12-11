from genesys.generator import NameGenerator


class BansheeNameGenerator(NameGenerator):
    data = [
        ["Abandoned","Aching","Agony","Anguish","Anguished","Bawling","Bitter","Blaring","Blind","Bloodied","Bloody","Broken","Burning","Cackling","Craven","Crazed","Crying","Dark","Deafening","Depraved","Deranged","Dire","Distressed","Drained","Dread","Dreadful","Enraged","Evanescent","Faded","Fading","Flustered","Forsaken","Frail","Grave","Grieving","Grievous","Grim","Haunted","Haunting","Heartrending","Heartsick","Hollow","Hopeless","Howling","Humming","Hurt","Hysterical","Ivory","Lamenting","Lone","Lonely","Lost","Mad","Maniacal","Manic","Mewling","Miserable","Misery","Moaning","Mournful","Mourning","Praying","Ringing","Roaming","Screaming","Screeching","Searching","Seeking","Shadowy","Shady","Shrieking","Silver","Sinister","Skeletal","Skinny","Slivery","Sniveling","Sobbing","Sorrowing","Sorrowing","Spiteful","Tearful","Torment","Tormented","Tortured","Vengeful","Vexed","Vicious","Wailing","Wandering","Warped","Waving","Weeping","Whimpering","Whining","Wicked","Woeful","Worn","Wretched","Yammering","Yelling","Yelping"],
        ["Apparition", "Banshee", "Bride", "Bridesmaid", "Dame", "Damsel", "Daughter", "Gal", "Girl", "Lady", "Maid",
         "Maiden", "Matriarch", "Matron", "Mother", "Nurse", "Priestess", "Soul", "Specter", "Spirit", "Widow", "Woman",
         "Wraith", "Angel", "Lover", "Fiancee", "Child", "Youth", "Aunt"],
    ]

    @classmethod
    def make_name(cls, parts):
        return "The {} {}".format(*parts)


def banshee_name_generate():
    return BansheeNameGenerator.generate()
