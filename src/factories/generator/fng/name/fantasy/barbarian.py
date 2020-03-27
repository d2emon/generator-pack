nm1 = ["ae","au","ei","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u"]
nm2 = ["","","","b","bl","br","bh","d","dr","dh","f","fr","g","gh","gr","gl","h","hy","hr","j","k","kh","kr","l","ll","m","n","p","pr","r","rh","s","sk","sg","sm","sn","st","t","th","thr","ty","v","y"]
nm3 = ["bl","br","d","db","dbr","dd","ddg","dg","dl","dm","dr","dv","f","fd","fgr","fk","fl","fn","fr","fst","fv","g","gb","gd","gf","gg","ggv","gl","gn","gr","gss","gv","k","kk","l","lb","lc","ld","ldr","lf","lfr","lg","lgr","lk","ll","llg","llk","llv","lm","ln","lp","lr","ls","lsk","lsn","lst","lsv","lt","lv","m","md","mk","ml","mm","ms","n","nb","nd","ndr","ng","nl","nn","nng","nr","nsk","nt","nv","nw","p","pl","pp","pr","r","rb","rd","rdg","rf","rg","rgr","rk","rkm","rl","rls","rm","rn","rng","rngr","rnh","rnk","rns","rnv","rr","rst","rt","rth","rtm","rv","s","sb","sbr","sg","sgr","sk","sl","sm","sn","sr","ssk","st","stm","str","sv","t","tg","th","thg","thn","thr","thv","tm","tr","tt","ttf","tv","v","yv","z","zg","zl","zn"]
nm4 = ["d","dr","f","g","kr","k","l","ld","lf","lk","ll","lr","m","mm","n","nd","nn","r","rd","rn","rr","s","th","t"]
nm5 = ["","","","b","br","bh","ch","d","dh","f","fr","g","gh","gr","gw","gl","h","j","k","kh","m","n","r","rh","s","sh","st","sv","t","th","thr","tr","v","w"]
nm6 = ["ae","ea","ie","ei","io","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u"]
nm7 = ["bj","c","d","dd","df","dl","dr","f","ff","fl","fn","fr","fth","g","gd","gm","gn","gnh","gr","h","hh","k","l","ld","lf","lfh","lg","lgr","lh","lk","ll","lm","lr","ls","lv","m","mm","n","nd","ndr","ng","ngr","ngv","nh","nl","nn","nnh","nr","ns","nt","nv","r","rd","rf","rg","rgh","rgr","rh","rk","rl","rm","rn","rnd","rng","rr","rst","rt","rth","rtr","rv","s","sb","sd","sg","sh","sl","st","stn","str","sv","t","thr","tk","tr","tt","tth","v","y","yj","ym","yn"]
nm8 = ["","","","","f","g","h","l","n","nn","s","sh","th","y"]




"""
FEMALE

rnd = Math.floor(Math.random() * nm5.length);
rnd2 = Math.floor(Math.random() * nm6.length);
rnd3 = Math.floor(Math.random() * nm8.length);
if(i < 3){
}else if(i < 8){
}else{
}
"""

import random
from factories.name import NameFactory, random_generator, genders


class BarbarianNameGenerator(NameFactory):
    base_data = {
        GENDER_MALE: [
            nm2,
            nm1,
            nm4,
        ],
        GENDER_FEMALE: [
            nm5,
            nm6,
            nm8,
        ],
    }
    data = {
        GENDER_MALE: [],
        GENDER_FEMALE: [],
    }

    @classmethod
    def generate_parts(cls, gender=GENDER_MALE, *args, **kwargs):
        parts = [random.choice(parts) for parts in cls.base_data[gender]]
        return parts[:-1] + [random.choice(part) for part in cls.data[gender]] + [parts[-1]]


class Barbarian1NameGenerator(BarbarianNameGenerator):
    @classmethod
    def update_parts(cls, parts, gender=GENDER_MALE, *args, **kwargs):
        if gender == GENDER_FEMALE:
            while cls.base_data[gender][0].index(parts[0]) < 5:
                parts[0] = random.choice(cls.base_data[gender][0])
        return parts


class Barbarian2NameGenerator(BarbarianNameGenerator):
    """
    """
    data = {
        GENDER_FEMALE: [
            nm7,
            nm6,
        ],
        GENDER_MALE: [
            nm3,
            nm1,
        ],
    }

    @classmethod
    def update_parts(cls, parts, gender=GENDER_MALE, *args, **kwargs):
        if gender == GENDER_FEMALE:
            if cls.base_data[gender][1].index(parts[1]) < 5:
                while cls.data[gender][1].index(parts[3]) < 5:
                    parts[3] = random.choice(cls.data[gender][1])
        else:
            if cls.base_data[gender][0].index(parts[0]) < 3:
                while cls.data[gender][1].index(parts[3]) < 3:
                    parts[3] = random.choice(cls.data[gender][1])
        return parts


class Barbarian3NameGenerator(BarbarianNameGenerator):
    """
    """
    data = {
        GENDER_FEMALE: [
            nm7,
            nm6,
            nm7,
            nm6,
        ],
        GENDER_MALE: [
            nm3,
            nm1,
            nm3,
            nm1,
        ],
    }

    @classmethod
    def update_parts(cls, parts, gender=GENDER_MALE, *args, **kwargs):
        if gender == GENDER_FEMALE:
            if cls.base_data[gender][1].index(parts[1]) < 5:
                while cls.data[gender][0].index(parts[3]) < 5:
                    parts[3] = random.choice(cls.data[gender][0])
            if cls.base_data[gender][1].index(parts[1]) < 5 or cls.data[gender][1].index(parts[3]) < 5:
                while cls.data[gender][5].index(parts[5]) < 5:
                    parts[5] = random.choice(cls.data[gender][5])
            parts = parts[:-1]
        else:
            if cls.base_data[gender][0].index(parts[0]) < 3:
                while cls.data[gender][1].index(parts[3]) < 3:
                    parts[3] = random.choice(cls.data[gender][1])
            if cls.base_data[gender][0].index(parts[0]) < 3 or cls.data[gender][1].index(parts[3]) < 3:
                while cls.data[gender][3].index(parts[5]) < 3:
                    parts[5] = random.choice(cls.data[gender][3])
        return parts


def barbarian_selector(generator_id):
    if generator_id < 3:
        return Barbarian1NameGenerator
    elif generator_id < 8:
        return Barbarian2NameGenerator
    return Barbarian3NameGenerator


def barbarian_name_generate(generator_id=None, gender=GENDER_MALE):
    return random_generator(barbarian_selector, generator_id=generator_id).generate(gender)
