import random
from v1.fng.genesys.name_factory import NameFactory, GenderNameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data
from v1.fng.genesys.genders import MALE, FEMALE


nm1 = ["Aka", "Ake", "Aki", "Ara", "Ari", "Ashi", "Ata", "Atsu", "Azu", "Bai", "Benji", "Bo", "Bunra", "Chi", "Cho", "Dai", "Do", "Enno", "Fu", "Fuku", "Fumi", "Ge", "Go", "Ha", "Hachi", "Hara", "Hi", "Hide", "Hiro", "Hisa", "Ho", "Hoku", "Hyo", "Ichi", "Ine", "Iso", "Ja", "Jinza", "Jo", "Juni", "Ka", "Kage", "Kama", "Kanza", "Katsu", "Kawa", "Kazu", "Ke", "Kei", "Kiyo", "Ko", "Koju", "Ku", "Kuni", "Kyo", "Kyu", "Ma", "Mamo", "Mana", "Mare", "Masa", "Mata", "Matsu", "Mitsu", "Miya", "Mo", "Monta", "Moro", "Moto", "Mu", "Mune", "Na", "Naga", "Naka", "Nari", "Naru", "No", "Nobo", "Nobu", "Nori", "Oka", "Oki", "Ori", "Ra", "Ri", "Ryu", "Sa", "Sada", "Saku", "Sei", "Sha", "Shi", "Shini", "Shinza", "Sho", "Shu", "So", "Suke", "Sumi", "Ta", "Tada", "Tadi", "Taka", "Take", "Tama", "Tamu", "Tatsu", "To", "Toki", "Tomo", "Toyo", "Tsu", "Tsuga", "Tsune", "Tsura", "Uta", "Ya", "Yaka", "Yasu", "Yo", "Yori", "Yoshi", "Yu", "Yugo", "Yusu"]
nm2 = ["baru", "bei", "bo", "boru", "buchi", "bumi", "buro", "busuke", "chi", "chiro", "chu", "daira", "dao", "dashi", "dasu", "don", "fumi", "fusa", "gai", "gawa", "geru", "ginori", "goro", "gumi", "gumichi", "hachi", "haku", "haru", "hashi", "hei", "hhiko", "hi", "hide", "hiko", "hira", "hiro", "hisa", "hito", "jiro", "juro", "ka", "kan", "kao", "kashi", "kasu", "kazu", "ke", "ken", "keno", "ki", "kichi", "kio", "kira", "kishi", "kko", "ko", "koji", "koto", "kuhei", "kumi", "kumo", "kuni", "kuro", "kusho", "mao", "mara", "maro", "masa", "masu", "matsu", "mba", "mei", "meisetsu", "michi", "mio", "mitsu", "mochi", "momi", "mon", "mori", "moru", "moto", "muku", "mune", "muro", "naga", "naka", "nao", "nari", "ne", "nibu", "nji", "njiro", "nkei", "nmochi", "nobu", "nokoji", "nore", "nori", "noru", "npachi", "npaku", "nsei", "nso", "ntaro", "pachi", "rai", "raku", "rao", "rata", "razo", "rei", "reo", "ri", "rio", "ro", "robei", "romao", "ruki", "ruko", "rumi", "sa", "saburo", "sai", "sake", "saki", "saru", "sashi", "sato", "sayuki", "seki", "shai", "shi", "shida", "shige", "shiki", "shin", "shiro", "shisai", "sho", "sine", "ssai", "su", "suke", "sumu", "tada", "taka", "take", "tan", "tane", "taro", "taru", "teru", "toki", "tomi", "tomo", "tomu", "tora", "toru", "toshi", "tsu", "tsugu", "tsuna", "tsune", "tsuya", "tsuzan", "yaki", "yasu", "yori", "yoshi", "yuki", "zan", "zane", "zen", "zo", "zushi"]
nm3 = ["A", "Ai", "Aki", "Ako", "Ama", "Ane", "Ari", "Asa", "Asu", "Atsu", "Aya", "Azu", "Chi", "China", "Do", "E", "Emi", "Etsu", "Fu", "Fumi", "Fuyu", "Gi", "Ha", "Hai", "Hani", "Haru", "Hazu", "Hi", "Hika", "Hime", "Hiro", "Ho", "Hono", "Hoshi", "I", "Ichi", "Ima", "Ina", "Iri", "Isa", "Itsu", "Jo", "Ka", "Kaho", "Kai", "Kame", "Kami", "Kane", "Kasu", "Katsu", "Kaza", "Kazu", "Ki", "Kimi", "Kinu", "Kio", "Kira", "Kiyo", "Ko", "Kochi", "Koha", "Koma", "Kono", "Koza", "Ku", "Kuki", "Kuru", "Kyo", "Ma", "Machi", "Mae", "Maki", "Mari", "Masu", "Matsu", "Mayo", "Me", "Michi", "Mido", "Miho", "Mika", "Mili", "Mine", "Misa", "Mitsu", "Natsu", "Ni", "No", "Ori", "Osa", "Ra", "Rai", "Rei", "Ri", "Rina", "Ru", "Ruri", "Ryo", "Sa", "Sai", "Saki", "Saku", "Sana", "Sawa", "Sayo", "Shi", "Shiho", "Shiru", "Su", "Sumi", "Suzu", "Ta", "Tada", "Taka", "Tama", "Tana", "Tani", "Tatsu", "Te", "To", "Toki", "Tomi", "Tomo", "Toshi", "Tsu", "Tsuki", "U", "Ume", "Ura", "Ure", "Usa", "Utsu", "Wa", "Waka", "Ya", "Yasu", "Yoshi", "Yu", "Yumi"]
nm4 = ["chi", "chiko", "chiru", "diri", "doka", "dori", "fumi", "fuyu", "gami", "gi", "gisa", "hana", "haru", "ho", "homi", "hori", "kari", "kayo", "kemi", "keno", "ki", "kichi", "kiko", "ko", "kumi", "kura", "kuri", "machi", "maki", "mami", "mari", "me", "meki", "meko", "mi", "miju", "mika", "miko", "mo", "momi", "na", "nako", "nami", "nari", "nase", "natsu", "ne", "neko", "ni", "niko", "no", "nomi", "noue", "nri", "nuye", "ra", "rabi", "rako", "rari", "ri", "riko", "rime", "risa", "rise", "ru", "rumi", "ruri", "sa", "sagi", "sago", "saki", "sami", "sato", "se", "shi", "shiko", "su", "suki", "sumi", "tako", "to", "tomi", "tori", "tose", "tsu", "tsuki", "tsumi", "tsune", "tsuyo", "tu", "wara", "ya", "yama", "yoko", "yomi", "yoshi", "yumi", "ze", "zomi", "zu", "zuka", "zuki", "zume", "zumi"]
nm5 = ["A", "Ada", "Aga", "Ai", "Aka", "Aki", "Ama", "Ame", "Ami", "Ara", "Ari", "Asa", "Ashi", "Azu", "Chi", "De", "Do", "Ebi", "Eda", "Ena", "Eno", "Fu", "Fuchi", "Fuji", "Fuku", "Furu", "Ha", "Hagi", "Hama", "Hana", "Hara", "Hari", "Hashi", "Hata", "Haya", "Hi", "Higa", "Hira", "Hiro", "Hisa", "Ho", "Hori", "Ichi", "Iga", "Ike", "Ima", "Ina", "Ise", "Ishi", "Iso", "Iwa", "Izu", "Ka", "Kaga", "Kagu", "Kami", "Kana", "Kane", "Kashi", "Kata", "Katsu", "Kawa", "Kaze", "Ki", "Kino", "Kiri", "Ko", "Koba", "Koda", "Komo", "Koni", "Koya", "Ku", "Kuma", "Kuri", "Kuro", "Kuwa", "Ma", "Maki", "Mana", "Maru", "Masa", "Masu", "Matsu", "Mawa", "Mi", "Mina", "Mitsu", "Miya", "Mizu", "Mo", "Mochi", "Mori", "Moto", "Mu", "Mura", "Na", "Naga", "Naka", "Nari", "Natsu", "Ni", "Nishi", "No", "Oga", "Oha", "Oka", "Oki", "Oku", "Omo", "Ona", "Osa", "Oshi", "Oto", "Otsu", "Ra", "Raku", "Ri", "Riki", "Sa", "Saka", "Saki", "Saku", "Se", "Seki", "Shi", "Shino", "Shira", "Sho", "So", "Su", "Suga", "Sugi", "Sumi", "Suzu", "Ta", "Taha", "Taka", "Take", "Tani", "Tate", "Tatsu", "To", "Tomi", "Tsu", "Ubu", "Uchi", "Ume", "Ura", "Uye", "Uzu", "Wa", "Waka", "Waki", "Waku", "Ya", "Yada", "Yaku", "Yama", "Yana", "Yashi", "Yasu", "Yori", "Yoshi", "Yu", "Za", "Zaka"]
nm6 = ["ba", "bara", "baru", "bashi", "bata", "be", "bi", "bira", "bu", "buki", "buto", "chi", "da", "date", "dera", "fumi", "ga", "gae", "gai", "gaki", "gami", "gata", "gawa", "gi", "gimoto", "giri", "gisawa", "gishi", "gita", "gome", "guchi", "gusa", "hara", "hata", "haya", "hei", "hira", "hisa", "hoshi", "jima", "ka", "kaga", "kaki", "kama", "kami", "kawa", "kaze", "ken", "ki", "kida", "kino", "kiri", "kita", "kite", "kono", "kuda", "kuma", "kura", "kuro", "kuwa", "ma", "machi", "maki", "mano", "mari", "maru", "matsu", "maya", "me", "mi", "mida", "mine", "misu", "mitsu", "miya", "mo", "mori", "moto", "mura", "muro", "naba", "naga", "nagi", "naha", "naka", "nari", "nashi", "nda", "ndo", "ne", "nen", "ni", "nishi", "no", "nobu", "noda", "numa", "ra", "rada", "ragi", "raki", "rano", "rata", "ri", "rima", "ro", "roma", "runo", "ruta", "saka", "saki", "sano", "sari", "sato", "sawa", "se", "shi", "shiba", "shida", "shige", "shima", "shino", "shiro", "shita", "sho", "sone", "su", "suchi", "suda", "sugi", "ta", "tagi", "taka", "take", "taki", "tanda", "tani", "tase", "to", "tomi", "tsami", "tsu", "tsuka", "tsuki", "tsumi", "wa", "wagi", "wara", "wari", "wata", "ya", "yama", "yashi", "yomi", "yoshi", "yuki", "za", "zaka", "zaki", "zato", "zawa", "ziwa", "zora", "zuki", "zuma", "zumi", "zuno"];\


# Models


class AnimeName(Name):
    @property
    def value(self):
        return f"{self.items[3]}{self.items[4]} {self.items[1]}{self.items[2]}"


# Factory


class AnimeNameFactory(GenderNameFactory):
    """Anime Character Name Factory"""

    class MaleAnimeNameFactory(NameFactory):
        name_class = AnimeName
        blocks_map = {
            1: 1,
            2: 2,
            3: 5,
            4: 6,
        }

        def validate(self, items) -> dict:
            item = str(items[1])
            return {
                0: random.choice(item[0]),
                1: random.choice(item[1]),
            }

    class FemaleAnimeNameFactory(NameFactory):
        name_class = AnimeName
        blocks_map = {
            1: 3,
            2: 4,
            3: 5,
            4: 6,
        }

        def validate(self, items) -> dict:
            item = str(items[1])
            return {
                0: random.choice(item[0]),
                1: random.choice(item[1]),
            }

    description = """Anime and manga character names typically fall into one of three categories: real names, fake names
        and unique or nicknames. Real names are usually just regular Japanese names, but can be from other cultures too
        depending on the anime. Nicknames and unique names tend to be very specific and often belong to the main
        character, like Ichigo from Bleach, Light from Death Note, or Naruto from Naruto.
        The fake names, which this generator focuses on, are similar to regular Japanese names, but you generally
        wouldn't find them in real life. Sometimes they're used to add a fantasy feeling to a story, sometimes they're
        used to avoid (accidental) matches with real life people, especially if a character is portrayed in a negative
        way, and other times it may be a more personal choice of the writer. Either way, this generator will generate a
        whole range of fake Japanese name fit for those types of anime and manga characters.
        Like regular Japanese names, the names in this generator are in surname - personal name order."""
    factory_classes = {
        MALE: MaleAnimeNameFactory,
        FEMALE: FemaleAnimeNameFactory,
    }
    default_blocks = load_data({
        1: nm1,
        2: nm2,
        3: nm3,
        4: nm4,
        5: nm5,
        6: nm6,
    })
