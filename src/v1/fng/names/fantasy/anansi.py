import random
from v1.fng.genesys.name_factory import NameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data

names1 = ["ákron", "ám̀ma", "ámmá", "ɔkwán", "abénaa", "aba", "abaka", "abeberese", "abena", "abenaa", "abeyie", "ablá",
          "ablã", "aboagye", "aboah", "aborah", "aborampah", "abrafi", "abrefa", "abrema", "achamfour", "acheampong",
          "ackon", "acquah", "adade", "addai", "addo", "adiyiah", "adjoa", "adjowa", "adjua", "adofo", "adomah",
          "adomako", "adusei", "adwoa", "adwubi", "afí", "afúom", "afful", "afiríyie", "afirifa", "afoakwah",
          "afrakoma", "afrakomah", "afram", "afrane", "afreh", "afrifa", "afriyie", "afua", "agyapong", "agyare",
          "agyei", "agyeman", "agyemang", "agyenim", "ahinful", "ajwoba", "akúá", "akú", "akaminko", "akenten",
          "akenteng", "akomeah", "akomfrah", "akosah", "akosi", "akosiwa", "akosua", "akoto", "akrofi", "akua",
          "akuamoah", "akuba", "akuffo", "akun", "akwasi", "akyaw", "ama", "amakye", "amamfo", "amankona", "amankonah",
          "amankwah", "amba", "ame", "ameyaw", "ameyo", "ami", "amissah", "amoabeng", "amoah", "amoako", "amoateng",
          "amofah", "ampadu", "ampem", "ampofo", "amponsah", "amponsem", "anúm", "anané", "anan", "andoh", "ankobiah",
          "ankomah", "ankrah", "annan", "anokye", "ansah", "ansong", "antó", "apau", "appiah", "araba", "arko",
          "arkorful", "así", "asón", "asamoah", "asante", "asantewaa", "asare", "asenso", "ashia", "asiamah", "asiedu",
          "asomadu", "asomaning", "assifuah", "asubonteng", "atá", "ataá", "ato", "awotwe", "awotwie", "awuah", "ayawa",
          "ayeh", "ayensu", "ayew", "bótwe", "baaba", "baafi", "baah", "baako", "badú", "badúwaa", "baffoe", "bafuor",
          "baidoo", "banahene", "barwuah", "bedíàkṍ", "bediako", "bedu", "bekṍe", "bekoe", "bemah", "berko", "boadi",
          "boadu", "boahen", "boakye", "boamah", "boampong", "boasiako", "boatei", "boateng", "bonah", "bonsra",
          "bonsrah", "bonsu", "brempong", "busia", "busiah", "cofie", "crentsil", "cudjoe", "cuffee", "dúkũ", "dúnu",
          "daako", "dankwah", "danquah", "danso", "dapaa", "dapaah", "darko", "dede", "dedei", "diawuo", "djan",
          "djansi", "domfe", "donkor", "dorkenoo", "duah", "dufie", "duodu", "dwamena", "dwamenah", "dwomoh", "ebo",
          "efia", "efua", "ekow", "ekua", "ekuoba", "enninful", "esi", "essien", "esson", "farkyi", "fiifi", "firikyi",
          "fofie", "fokuo", "fordjour", "forobuor", "fredua", "freduah", "fremah", "frempon", "frempong", "frimpong",
          "gaddo", "gyaama", "gyakari", "gyamah", "gyambibi", "gyamera", "gyamerah", "gyamfi", "gyan", "gyasi",
          "gyeabuor", "gyimah", "inkoom", "jojo", "kaakyire", "kaku", "kande", "karikari", "katakyie", "kenu", "kodjó",
          "koduah", "kofí", "koffi", "kofi", "kojo", "kokote", "kokou", "koku", "komi", "komlá", "komlã", "komlan",
          "konadu", "koranten", "koranteng", "korsah", "kosi", "kouassi", "kow", "kuffour", "kufuor", "kumankama",
          "kumi", "kusi", "kusiwaa", "kuuku", "kuwame", "kwámè", "kwǎmè", "kwaata", "kwabená", "kwadwó", "kwakú",
          "kwakye", "kwamena", "kwami", "kwamina", "kwarteng", "kwasí", "kwasiba", "kwateng", "kwaw", "kwayie", "kweku",
          "kwesi", "kyei", "kyekyeku", "kyem", "kyerematen", "kyeremateng", "kyereme", "kyerewa", "kyerewaa", "máanu",
          "mánsã", "mǎnu", "mansah", "manso", "meńsã́", "mensah", "mintah", "misa", "mmorosa", "mpong", "munuo", "núm",
          "narh", "nduom", "nimo", "nimoh", "nkansa", "nkansah", "nkróma", "nkrumah", "nsĩã́", "nsṍwaa", "nsiah",
          "nsonwaa", "nsonwah", "nsor", "ntiamoa", "ntiamoah", "ntim", "ntow", "nuamah", "nyaméama", "nyamékyε",
          "nyamekye", "nyankómàgó", "nyankomago", "nyantah", "nyantakyi", "nyarko", "obím̀pέ", "obeng", "obuor",
          "oduro", "ofori", "ofosu", "ogyampah", "ohemeng", "ohene", "okese", "okoromansah", "okyere", "omenaa",
          "omenah", "opambuor", "opare", "opoku", "oppong", "opuni", "osafo", "osam", "osei", "oteng", "otuo",
          "owoahene", "owusu", "oyiakwan", "píèsíe", "paintsil", "pappoe", "peprah", "pinaman", "poku", "prempeh",
          "quainoo", "quansah", "safo", "sakyi", "sarfo", "sarkodie", "sarpei", "sarpon", "sarpong", "sasraku",
          "siabuor", "siaw", "siisi", "sika", "sikafuo", "sintim", "siriboe", "soadwa", "soadwah", "sowah", "táwia",
          "tagoe", "takyi", "tandoh", "tawiah", "tuffour", "twasam", "tweneboa", "tweneboah", "twerefuo", "twum",
          "twumasi", "vorsah", "wiafe", "wiredu", "yεmpέw", "yaa", "yaaba", "yaba", "yamoah", "yankah", "yao", "yartei",
          "yaw", "yawo", "yeboah", "yiadom", "yoofi"]


# Models

class AnansiName(Name):
    vowels = ["a", "e", "i", "o", "u", "á", "ã", "í", "ú", "é", "ó"]

    @property
    def value(self):
        vowels_count = 0
        if self.items[0][-1] in self.vowels:
            vowels_count += 1
        if self.items[2][0] in self.vowels:
            vowels_count += 1

        if vowels_count == 2 and len(self.items[2]) > 1:
            name_final = self.items[2][2:] if self.items[2][1] in self.vowels else self.items[2][1:]
        elif vowels_count == 1:
            name_final = self.items[2]
        else:
            name_final = f"{self.items[1]}{self.items[2]}"

        return f"{self.items[0]}{name_final}"


# Factory

class AnansiNameFactory(NameFactory):
    """Anansi Name Factory"""

    description = """Anansi is a spider or spider-like trickster originating in Akan folklore, but it can also be found
        in Ashanti, Jamaican and Surinamese folklore. Despite being a trickster, he is often celebrated as a cunning and
        wise protagonist within his stories. Anansi is able to overcome stronger opponents through wit and cunning.
        Stories of the Anansi were passed on orally and survived the slave trade. In fact, it was a popular story among
        enslaved Africans because of the Anansi's ability to overcome stronger opponents. Anansi became a symbol of
        resistance and survival.

        While there is only 1 Anansi within the stories, their name does differ at times (often based on language).
        Anansi is also often represented as having a family, though they're not named. This name generator serves as a
        way to find names for these types of trickster beings and focuses on names in an Akan style. The names aren't
        real, however, merely based on real Akan names. The idea behind it is to create names representing the
        supernatural more than the real, while still being tied to both sides.
        Alternatively, the spiderfolk could be of help to you, too. Depending on the type of name you're looking for."""
    default_blocks = load_data({
        1: names1,
        8: AnansiName.vowels,
    })
    blocks_map = {
        1: 1,
        3: 1,
        5: 8,
    }
    name_class = AnansiName

    def get_items(self) -> dict:
        items = super().get_items()
        return {
            1: items[1],
            2: random.randrange(len(items[1].value)),
            3: items[3],
            4: random.randrange(len(items[3].value)),
            5: items[5],
        }

    def validate(self, items) -> dict:
        # 2
        if items[2] < 1:
            items[2] = 1
        if (items[2] < 3) and (len(items[1]) > 4):
            items[2] = 3
        if items[2] > 5:
            items[2] = 5

        # 4
        if items[4] < 1:
            items[4] = 1
        if (items[4] < 3) and (len(items[3]) > 4):
            items[4] = 3
        if items[4] > 5:
            items[4] = 5

        # 2
        if (items[2] == 1) and (items[4] == 1):
            items[2] = 2

        return {
            0: items[1].value[:items[2]],
            1: items[5],
            2: items[3].value[items[4] - 1:],
        }
