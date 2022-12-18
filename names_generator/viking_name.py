import random

# todo: process all this names:
# vikings = [["Ake","ancestor"],
# ["Aart", ["powerful as an eagle","eagle-like"]],
# ["Adelmar" - noble strength/character,],
# ["Addelmar" - noble strength/character,],
# ["Athelmar" - noble strength/character,],
# ["Aelram" - dark and noble,],
# ["Aegir" - water giant,],
# ["Aesir" - god,],
# [(A/Ö)gmund(r/ur) awe or terror/edge or sword-warded/protected,],
# ["Agnarr" - awe or terror/edge or sword-warrior,],
# [Alari(c/ch/k) - emperor/king of all/all-powerful ruler,],
# ["Albrecht" - noble and bright,],
# [Al(d)ri(c/ch/k) - wise sage/noble ruler,],
# ["Alois"/"Hlödvig" - loud/famous fight/battle/warrior,],
# ["Alfhar" - elf warrior,],
# ["Alvar"/"Alvge"(i/y)r( r) - elf spear,],
# ["Anders" - manly, brave, strong,],
# [A(n)sg(a/ei)r( r) - god-spear,],
# ["Arjac" - meaning unknown,],
# ["Arlen" - vow/oath/pledge,],
# [Arn(e) - eagle,],
# [Asvald( r) - divine ruler/might/power,],
# ["Atli" - Terrible, violent, wild,],
# ["Audun" - friend of wealth,],
# ["Aun" - possibly shortened name meaning ‘friendly destiny’,],
# [Avang(r/er) - meaning unknown,],
# [Bald(e/u)r - prince/god-son/light-bearer,],
# ["Barend" - as brave as a bear,],
# ["Beoric" - bright power,],
# ["Bertram" - bright as a raven,],
# [B(e/i/y)r(g/gh)(e/i/y)r - one who helps or protects/keeper,],
# [Bj(o/ö)rn - bear,],
# [Bj(o/ö)rnst(e/ei/y)n - stone bear or bear-stone,],
# ["Bodvar" - battle-army,],
# ["Borgen" - from a fort town, castle,],
# ["Bran" - raven,],
# [Bran(d/t/dt)( r) - sword/fIre/torch/burning log or pole,],
# ["Brynjar" - armored/helmed warrior,],
# ["Brynulf" - armored/mailed wolf,],
# ["Calder" - harsh and cold waters,],
# ["Canis" - dog,],
# ["Cord" - bold/wise counselor,],
# ["Dag" - day,],
# ["Dagrún" - day-secret/lore,],
# [Dol(f/ph) - noble wolf,],
# ["Drekken" - dragon/drake,],
# [Dren(n) - meaning unknown,],
# [(Dur/T(h)or)fast - firm/strong thunder,],
# ["Dvordin" - meaning unknown; likely based on Dvergr (dwarf),],
# ["Eberhard" - courageous like a boar,],
# ["Edvard" - wealthy guard/protector,],
# ["Ehren" - unclear, hidden,],
# ["Egil" - inspires fright; awe,],
# ["Egon" - strong with a sword,],
# [Einar( r) - one who fights alone,],
# ["Einrid" - one who rides alone,],
# ["Eluf" - eternal heir,],
# ["Engir" - meaning unknown,],
# [(E/Ei)r(i/y)(c/k/g/gh) - king of all/forever,],
# ["Erlend" - outsider/foreigner,],
# ["Erling"/"Ernil" - prince (Ernil is Sindarin - Tolkein's elven language),],
# ["Eyvindur" - fortune’s victor,],
# [Faf(fnr/nir) - dragon,],
# ["Félagi" - fellow/partner,],
# ["Fell" - living in the mountains/from the rough hill,],
# ["Fergus" - man of force/wrath; strong/virile,],
# [Fenr(i/y)(d/k/r/s) - world name/fen dweller,],
# [Fin(n/nr/r) - Wanderer/wandering,],
# ["Fjolnir" - concealer, wise one, manifold,],
# [Fj(o/y)r - life, spirit,],
# ["Forni" - ancient one,],
# ["Fraridr" - the one who rides forth,],
# [Frey( r) - lord,],
# ["Fritjof" - thief of peace,],
# [Frodar( r) - wise warrior,],
# [Frode/Frodi - enlightened/wise,],
# ["Ganglar" - wayweary,],
# ["Geigor"/"Greger" - watchful, alert,],
# [Ge(i/y)r( r) - spear,],
# ["Gilen" - vow/oath,],
# [Gn(j)arl/Gnyrll - snarl/growl; twisted up,],
# [Go(d/t/tt)( b )ran(d/t/dt)( r)/Gul(l)bran(d/t/dt)( r) - god-sword/fire,],
# [Go(d/dd/t/th)r(i/o)(c/k/g/gh) - power of god,],
# [Grim( r)/Gri(m/v)nir - grim, cruel; masked/hooded,],
# [Gung(n)ir - god-spear/swaying one,],
# [Gunn(a/i)r - brave and bold; warrior,],
# ["Gunnulf" - battle/war wolf,],
# ["Gunvald" - war leader,],
# ["Gunvor" - vigilant in war/battle,],
# ["Hagan" - briar,],
# ["Hákon"/"Hakon"/"Haakon"/"Hågen" - high or highest son,],
# ["Haldor" - thunder stone/god-stone,],
# ["Halvard" - rock/stone guardian,],
# ["Havard" - high guardian,],
# ["Harald" - army leader/war chief,],
# [Har(e/i/y)(c/k/g/gh) - high sovereign,],
# [Hauk( r) - hawk,],
# [Heimdal(l)( r) - shining god/guardian of the shining bridge,],
# ["Helgan" - sainted,],
# [Helg(e/i) - holy/blessed,],
# ["Hemming" - shape-changer,],
# ["Hengir" - hone-spear,],
# [Hengis(t) - stallion,],
# ["Herleif" - warrior descendent,],
# ["Herulf"/"Hjorulf" - sword wolf,],
# ["Hildulf" - battle wolf,],
# ["Hjalmar" - helmed fighter,],
# ["Holger" - island of spears,],
# [(H)rafn - raven,],
# [(H)r(o/u)l(f/ph) - renown/famous/well-known wolf,],
# [Hr(o/u)lfg(a/ei)r - wolf-spear,],
# [(H)rothgar - famous spear/defender,],
# [(H)rungnir - brawler,],
# ["Hundr" - hound,],
# ["Ingvarr" - holy warrior,],
# ["Yngvar" - holy warrior,],
# ["Ingfor" - divinely protected,],
# ["Ingvard" - divinely protected,],
# ["Ingvir" - divinely protected,],
# ["Ivar"( r) - fighter with a bow/archer,],
# [Jaeg(e)r - hunter,],
# ["Jari" - helmeted soldier,],
# ["Jarlulf" - chief wolf/wolf lord,],
# ["Jarn" - iron,],
# ["Jarnulf" - iron wolf,],
# ["Jarnvid" - ironwood,],
# [Jokul(l) - ice, icicle, glacier,],
# [Jólf( r) - horse-wolf,],
# [Jor( r) - wild boar,],
# [Jor(g)(e/i/y)n - farmer/earth-worker,],
# ["Jormund" - sword-safe/protected from blades,],
# [Jori(c/k/g/gh) - mighty horse/ horse chieftain,],
# ["Jorund" - battle winner,],
# [(J/Y)otun(n) - jotun/giant/titan/troll/supernatural being,],
# ["Kennet" - born of fire,],
# [K(a/j/v)(a/y)rl - chief man,],
# ["Kjeld" - large pot,],
# ["Knut" - knot,],
# [(K/T)or( r)vald( r) - Thor’s ruler/chieftain,],
# [Kra(gh/k(u)r) - crow,],
# ["Krom" - Hyperborean (Robert E. Howard's Conan books) god of war,],
# [(K)veld(o/u)l(f/ph) - evening/night/twilight wolf,],
# [L(au/ei)f - son/descendant/heir,],
# [L(au/ei)fvar - heir-guard,],
# ["Logan" - little hollow,],
# ["Lothar" - famous army/warrior,],
# ["Lukas" - meaning unknown,],
# [Nils(en) - victorious/conqueror of the people,],
# [Nja( r)l - champion/giant,],
# ["Njord" - strong,],
# [(N/T)org(ei/i/y)r( r) - Thor’s spear or god-/thunder-spear,],
# [Od(ai/i/y)n(n) - high-god/chief god,],
# [O(dd/th)var - sharp point guard,],
# [(Oe/A)ngus - powerful/strong one,],
# ["Ofnir" - inciter,],
# [Ol(a/o)(f/v) - ancestor’s heir,],
# [Ol(i/y)n - hallowed,],
# [Olv(i/y)r - protected/lucky warrior,],
# [Or(i/y)n(n) - light, fair,],
# ["Orvar" - arrow,],
# ["Orven" - brave friend,],
# ["Otto" - wealthy, prosperous,],
# ["Ove" - full of terror,],
# ["Preben" - first in battle,],
# [R(a/ae/ei)g(e/i)r - heron,],
# ["Ragnar" - military advisor/war knowledge,],
# ["Rand" - shield-rim,],
# [Ran(u/o)l(f/ph) - wolf shield-rim,],
# ["Reidar" - home warrior,],
# [Ri(c/k/g/gh)ard - daring power,],
# [Ri(d/dd/th)ar - warrior on horse,],
# [R(h)uarc - rainstorm/squall,],
# [Run(v)ar( r) - secret lore (magic/rune) warrior,],
# [Runst(e/ei/u)n(er/r) - rune/lore/magic-stone,],
# [Ruri(c/k/g/gh) - famous power,],
# ["Rymr" - noise,],
# [S(a/o)lgeir( r) - sun-spear,],
# ["Sigurd" - victory guard,],
# ["Sigvald" - ruler of victory/victorious ruler,],
# [Skallagrim( r) - grim-skull,],
# ["Skander" - reaver/raider,],
# [Sk(j)old( r) - shield,],
# ["Snorri" - attack/onslaught,],
# ["Solvar"(r/d) - sun-protection/watchful sun,],
# ["Stal" - steel,],
# ["Stef" - crown,],
# [Ste(i)n - stone or small rock,],
# ["Stian"/"Stig"( r) - wanderer,],
# [Ste(i)nar( r) - stone warrior,],
# [St(o/u/y)rlaug(r/ur) - holy battle-oath,],
# [St(o/u/y)rbj(o/ö)rn - battle-bear,],
# [Sv(a/e)rd - sword,],
# ["Svarnir" - slayer,],
# [Svart(a)bran(d/t/dt)( r) - black blade/sword,],
# [Svart(a)g(ei/y)r( r) - black spear,],
# [Sven(d) - boy/youth,],
# [T(h)orgil/Korgil - Thor’s/god-shaft,],
# [T(h)or(o/u)l(f/ph) - Thor’s/god-wolf,],
# [T(h)or(ben/bj(o/ö)rn) - Thor's/god-bear,],
# [T(ore/hore/hor/har) - god/great/thunder-strength,],
# [T(h)or(f)in(n/nr) - Thor’s/god-wanderer,],
# [T(h)ormund( r) - Thor’s/god-protection,],
# [T(h)orvind( r) - Thor’s/god-victory/friend,],
# ["Troels"  "arrow of Thor/god"],
# ["Trygyv"  "trustworthy"],
# ["Tyge"  "one who hits the mark"],
# ["Ulbran" , "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulbranr" , "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulfbrand", "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulfbrant", "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulfbrandr" , "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulfbrantr" , "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulfbranr" , "wolf-sword/fIre/torch/burning log or pole"],
# ["Ulf" , "wolf"],
# ["Ulrik" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulric" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulrig" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulrigh" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulfric" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulfrik", "wealthy/powerful ruler; wolf ruler"],
# ["Ulfrig" , "wealthy/powerful ruler; wolf ruler"],
# ["Ulfrigh" , "wealthy/powerful ruler; wolf ruler"],
# ["Vaddr" , "ram/weather"],
# ["Vadher" , "ram/weather"],
# ["Var" , "ram/weather"],
# ["Væddr" , "ram/weather"],
# ["Vaædher" , "ram/weather"],
# ["Vær" , "ram/weather"],
# ["Veddr" , "ram/weather"],
# ["Vedher" , "ram/weather"],
# ["Vali" , "powerful/strong, chosen"],
# ["Veurr" , "shrine-guard/hallower"],
# ["Vidarr" , "warrior apart, wide warrior, killer"],
# ["Vidurr" , "warrior apart, wide warrior, killer"],
# ["Viggo" , "battle"],
# ["Vilmar" , "strong willed"],
# ["Vindar" , "victorious warrior/army"],
# ["Vindler" , "wind-sea"],
# ["Valdr" , "ruler, mighty one"],
# ["Valder" , "ruler, mighty one"],
# ["Volund" , "brave in battle, courageous warrior, skillful blacksmith"],
# ["Volundr" , "brave in battle, courageous warrior, skillful blacksmith"],
# ["Vygar", "powerful warrior/armor"],
# ["Yrungr" , "stormy"],
# ["Yrung" , "stormy"],
# ["Yngfor" , "divinely protected"],
# ["Yngvard" , "divinely protected"],
# ["Yngvir" , "divinely protected"]
# ]

"""Names=
Morkai
Lokyar
Roll Given Name
Roll Given Name
Roll Given Name
Roll Given Name"""

sample_names = ["Ake", "Aart", "Adelmar", "Addelmar", "Athelmar", "Aelram", "Aegir", "Aesir", "Agnarr", "Albrecht",
                "Alois", "Hlödvig", "Alfhar", "Alvar", "Alvge", "Anders", "Arjac", "Arlen", "Atli", "Audun", "Aun",
                "Barend", "Beoric", "Bertram", "Bodvar", "Borgen", "Bran", "Brynjar", "Brynulf", "Calder", "Canis",
                "Cord", "Dag", "Dagrún", "Drekken", "Dvordin", "Eberhard", "Edvard", "Ehren", "Egil", "Egon", "Einrid",
                "Eluf", "Engir", "Erlend", "Erling", "Ernil", "Eyvindur", "Félagi", "Fell", "Fergus", "Fjolnir",
                "Forni", "Fraridr", "Fritjof", "Ganglar", "Geigor", "Greger", "Gilen", "Gunnulf", "Gunvald", "Gunvor",
                "Hagan", "Hákon", "Hakon", "Haakon", "Hågen", "Haldor", "Halvard", "Havard", "Harald", "Helgan",
                "Hemming", "Hengir", "Herleif", "Herulf", "Hjorulf", "Hildulf", "Hjalmar", "Holger", "Hundr", "Ingvarr",
                "Yngvar", "Ingfor", "Ingvard", "Ingvir", "Ivar", "Jari", "Jarlulf", "Jarn", "Jarnulf", "Jarnvid",
                "Jormund", "Jorund", "Kennet", "Kjeld", "Knut", "Krom", "Logan", "Lothar", "Lukas", "Njord", "Ofnir",
                "Orvar", "Orven", "Otto", "Ove", "Preben", "Ragnar", "Rand", "Reidar", "Rymr", "Sigurd", "Sigvald",
                "Skander", "Snorri", "Solvar", "Stal", "Stef", "Stian", "Stig", "Svarnir", "Troels", "Trygyv", "Tyge",
                "Veurr", "Vidarr", "Vidurr", "Viggo", "Vilmar", "Vindar", "Vindler", "Valdr", "Valder", "Vygar",
                "Yngfor", "Yngvard", "Yngvir", ]

Ages = ["Ancient", "Elder", "Eternal", "Wizened", "Younger", "Young", "Youthful", "Youth"]
Storm = ["Storm", "Thunder", "Cloud", "Gale", "Lightning", "Mist", "Fog"]
Altered = ["Broken", "Cogged", "Gnarl", "Gnarled", "Hanged", "Shard", "Jagged"]
Animals = ["Aelf", "Aelvyn", "Crow", "Raven", "Foe", "Ork", "Troll", "Wolf", "Wulf", "Hound"]
Colors = ["Black", "Coal", "Ebon", "Blue", "Woad", "Grey", "Ashen", "Red", "Rust", "Rauð", "White", "Ivory", "Pale",
          "Yellow", "Amber", "Umber"]
Combat = ["Battle", "Dead", "Death", "Strife", "Unblooded", "War", "Wrath", "Wrathful"]
Direction = ["Close", "East", "Far", "North", "South", "West"]
Enemies = ["Daemon", "Devil", "Fiend", "Dragon", "Drake", "Wyrm", "Draugr", "Ghast", "Ghost", "Wraith", "Giant",
           "Jotun", "Yotun", "Kraken"]
Face = ["beard", "brow", "eyed", "gaze", "jaw", "maw", "chin", "lip", "nose"]
Give = ["fill", "filler", "granter", "grant", "make", "smith", "wright", "shaper", "shape", "accorder", "accord",
        "carver", "carve"]
Head = ["head", "headed", "lock", "mane", "skull", "ear", "ears", "earred", "crest"]
Fates = ["Wyrd", "Strange", "Bale", "Bane", "Doom", "Oath", "Fell"]
Fearful = ["Dark", "Dire", "Grim", "Shadow", "Silent", "Terror", "Fire=", "Ember", "Fire", "Fyr", "Flame", "Blaze",
           "Heat", "Hot", "Burn", "Scorch"]
Functions = ["Bard", "Skald", "Berserker", "Guard", "Priest", "Reaper", "Trickster"]
Heavens = ["Night", "Twilight", "Moon", "Dawn", "Dusk", "Sky", "Sun", "Star", "Void", "Aether"]
Hold = ["bind", "binder", "bound", "bring", "bringer", "grasp", "grasped", "grip", "gripper", "herd", "herder", "gird",
        "shackling"]
Hunt = ["hunt", "hunter", "seek", "seeker", "stalk", "stalker", "tracker", "courser", "harrier"]
Winter = ["Blizzard", "Frost", "Rime", "Ice", "Snow", "Winter", "Cold", "Frozen"]
Internals = ["blood", "bone", "breath", "sinew", "sinewed", "thews", "fang", "tooth", "tongue"]
Kinship = ["Born", "Brother", "Broder", "Kin", "Son", "Scar", "Scarred", "Skar", "Skarred"]
Limbs = ["arm", "claw", "fist", "hand", "handed", "foot", "footed", "wing", "leg", "Locations"]
Hel = ["Bog", "Fen", "Moor", "Sea", "Shore", "Hame", "Home", "Heim", "Field", "Feld", "Desert", "Barren"]
Measured = ["Long", "High", "Tall", "Proven", "Quick", "Swift", "Hard"]
Move = ["ride", "rider", "run", "runner", "stride", "strider", "walk", "walker", "wander", "wanderer", "skirr"]
Noise_making = ["call", "caller", "drum", "drummer", "howl", "howler", "speak", "speaker", "sing", "singer", "song",
                "sung", "sound", "sounder"]
Numbers = ["All", "Half", "Three", "Thrice", "Twice", "Two", "Twin"]
Earth = ["Forest", "Wood", "Cairn", "Cave", "Tree", "Timber", "Hill", "Mountain", "Iron", "Steel", "Rock", "Stone",
         "Earth"]
Sunder = ["break", "breaker", "cleave", "cleaver", "shatter", "shatterer", "split", "splitter", "strike", "striker",
          "wrack", "wracked"]
Things = ["Armor", "Mail", "Blade", "Hilt", "Helm", "Horn", "Saga", "Shield"]
Torso = ["back", "hide", "skin", "pelt", "pelts", "gore", "heart", "soul"]
Tools = ["Anvil", "Awl", "Gimlet", "Pick", "Bolt", "Forge", "Hammer", "Ship"]
Traits = ["Brash", "Fierce", "Mad", "Sly", "Wild", "Wyld", "Wise"]
Weapons = ["Axe", "Bow", "Dagger", "Knife", "Saber", "Spear", "Sword"]
Harm = ["destroy", "destroyer", "kill", "killer", "reave", "reaver", "rot", "rotting", "slay", "slayer", "slain",
        "smite", "smiter"]

lastname_list = [Ages, Storm, Altered, Animals, Colors, Combat, Give, Direction, Enemies, Face, Head, Fates, Fearful,
                 Functions, Heavens, Hold, Hunt, Winter, Internals, Kinship, Limbs, Hel, Measured, Noise_making,
                 Numbers, Earth, Sunder, Things, Torso, Tools, Traits, Weapons, Harm, ]

begginings = [Ages, Storm, Altered, Animals, Colors, Combat, Direction, Enemies, Fates, Fearful, Heavens, Winter,
              Internals, Kinship, Hel, Measured, Numbers, Earth, Things, Torso, Tools, Traits, Weapons]
endings = [Storm, Animals, Enemies, Face, Give, Head, Fates, Fearful, Functions, Hold, Hunt, Internals, Limbs, Move,
           Noise_making, Sunder, Things, Torso, Tools, Weapons, Harm]


class NameMe:

    def __init__(self, fullname=True, amount=1):

        self.fullname = fullname
        self.n = amount

        for _ in range(amount):
            self.name = NameMe.first_name()
            # noinspection SpellCheckingInspection
            self.lastname = NameMe.last_name()
            yield f"{self.name} {self.lastname}"

    def __repr__(self):
        pass

    @staticmethod
    def first_name():
        return random.choice(sample_names)

    @staticmethod
    def last_name():

        final_name = ""

        start = random.choice(begginings)
        end = random.choice(endings)
        begins = random.choice(start)
        ends = random.choice(end)

        final_name += begins.title()
        final_name += ends.lower()

        return final_name

    @staticmethod
    def generate_fullname(n=1):

        name_list = []
        for _ in range(n):

            firstname = NameMe.first_name()
            # noinspection SpellCheckingInspection
            lastname = NameMe.last_name()
            fullname = f"{firstname} {lastname}"
            name_list.append(fullname)

        if n > 1:
            return name_list
        return name_list[0]


if __name__ == '__main__':

    names = NameMe.generate_fullname(100)
    if type(names) == list:
        for name in names:
            print(name)
    else:
        print(names)
