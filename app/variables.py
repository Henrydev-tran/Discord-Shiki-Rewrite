import scripts.interactable as i
from scripts.Item import _vitem

# enemies
hilichurl = i._venemy__char(i._vbase__character(9000, 400, 340, 0, 0, 0, 0, 'pure', 'hilichurl', 0, 3))
blazeaxemi = i._venemy__char(i._vbase__character(24000, 2000, 450, 0, 0, 0, 0, 'pyro', 'blazing axe mitachurl', 0, 2))
woodshimi = i._venemy__char(i._vbase__character(35000, 1200, 1000, 0, 0, 0, 0, 'dendro', 'wooden shield mitachurl', 0, 2), True)
stonehidela = i._venemy__char(i._vbase__character(40000, 3000, 700, 0, 0, 0, 0, 'geo', 'stonehide lawachurl', 0, 1), True)
hydrosa = i._venemy__char(i._vbase__character(12000, 1400, 350, 0, 0, 0, 0, 'hydro', 'hydro samachurl', 0, 2))
cryosa = i._venemy__char(i._vbase__character(12000, 1400, 350, 0, 0, 0, 0, 'cryo', 'cryo samachurl', 0, 1))
hilichurlber = i._venemy__char(i._vbase__character(13000, 1750, 400, 0, 0, 0, 0, 'pyro', 'hilichurl berserker', 0, 1))
hilichurlar = i._venemy__char(i._vbase__character(9000, 800, 340, 0, 0, 0, 0, 'pure', 'hilichurl archer', 0, 2))
hilichurlarp = i._venemy__char(i._vbase__character(9000, 900, 340, 0, 0, 0, 0, 'pyro', 'hilichurl pyro archer', 0, 2))
hilichurlarc = i._venemy__char(i._vbase__character(9000, 800, 340, 0, 0, 0, 0, 'cryo', 'hilichurl cryo archer', 0, 2))

cryofgun = i._venemy__char(i._vbase__character(25000, 2000, 800, 0, 0, 0, 0, 'cryo', 'cryo fatui gunner', 0, 2), True)
hydrofgun = i._venemy__char(i._vbase__character(25000, 2000, 800, 0, 0, 0, 0, 'hydro', 'hydro fatui gunner', 0, 2), True)
pyrofsli = i._venemy__char(i._vbase__character(20000, 2000, 800, 0, 0, 0, 0, 'pyro', 'pyro fatui slinger', 0, 1), True)
geofcha = i._venemy__char(i._vbase__character(20000, 2000, 800, 0, 0, 0, 0, 'geo', 'geo fatui chanter', 0, 1), True)
anemofbox = i._venemy__char(i._vbase__character(32500, 2000, 800, 0, 0, 0, 0, 'anemo', 'anemo fatui boxer', 0, 2), True)
electfham = i._venemy__char(i._vbase__character(32500, 3000, 1000, 0, 0, 0, 0, 'electro', 'electro fatui vanguard', 0, 2), True)
electfcim = i._venemy__char(i._vbase__character(15000, 1500, 500, 0, 0, 0, 0, 'electro', 'electro fatui cicin mage', 0, 2), True)

#base characters
baseaether = i._vbase__character(14067, 1352, 300, 150, 40, 175, 275, 'anemo', 'aether', 0)
baseamber = i._vbase__character(16208, 1048, 500, 200, 10, 250, 350, 'pyro', 'amber', 0)
baselisa = i._vbase__character(12350, 1074, 400, 120, 30, 300, 750, 'electro', 'lisa', 0)
basekaeya = i._vbase__character(17505, 1202, 650, 350, 20, 180, 300, 'cryo', 'kaeya', 0)

guoba = i._vcharacter(i._vbase__character(999999, 9999, 9999, 99999, 100, 9999, 99999, 'pyro', 'guoba', 0), "god")
oz = i._vcharacter(i._vbase__character(999999, 9999, 9999, 99999, 100, 9999, 99999, 'electro', 'oz', 0), "god")

aether = i._vcharacter(baseaether, "support/sub-dps/dps")
_vaether_emoji = "<:traveller:1048802893483999252>"

amber = i._vcharacter(baseamber, "support")
_vamber_emoji = "<:amber:1048828854128615444>"

lisa = i._vcharacter(baselisa, "support")
kaeya = i._vcharacter(basekaeya, "dps/support")
gaether = i._vcharacter(i._vbase__character(14067, 1352, 300, 150, 40, 175, 275, 'geo', 'aether', 0), "support/sub-dps/dps")
eaether = i._vcharacter(i._vbase__character(14067, 1352, 300, 150, 40, 175, 275, 'electro', 'aether', 0), "support/sub-dps/dps")
xiangling = i._vcharacter(i._vbase__character(13946, 1402, 200, 170, 50, 250, 650, 'pyro', 'xiangling', 0), "dps")
bennett = i._vcharacter(i._vbase__character(11542, 1140, 400, 150, 60, 200, 500, 'pyro', 'bennett', 25000), "support/healer")
noelle = i._vcharacter(i._vbase__character(16946, 1032, 1072, 140, 30, 110, 350, 'geo', 'noelle', 16000), "support/healer")
xingqiu = i._vcharacter(i._vbase__character(13978, 1460, 200, 170, 50, 300, 450, 'hydro', 'xingqiu', 20000), "support/healer")
diona = i._vcharacter(i._vbase__character(12236, 1240, 500, 150, 60, 300, 400, 'cryo', 'diona', 25000), "support/healer")
zhongli = i._vcharacter(i._vbase__character(17046, 1532, 772, 200, 50, 140, 800, 'geo', 'zhongli', 0), "dps/support")
venti = i._vcharacter(i._vbase__character(17046, 1532, 772, 200, 50, 140, 800, 'anemo', 'venti', 0), "dps/support")
baal = i._vcharacter(i._vbase__character(17046, 1532, 772, 200, 50, 200, 700, 'electro', 'baal', 0), "dps/support")
eula = i._vcharacter(i._vbase__character(15087, 3057, 658, 400, 40, 200, 2000, 'cryo', 'eula', 0), "dps")

testitem = None

Games = []

enemiespossible = [hilichurl, stonehidela, blazeaxemi, woodshimi, cryosa, hydrosa, hilichurlar, hilichurlber, hilichurlarc, hilichurlarp, cryofgun, hydrofgun, pyrofsli, geofcha, anemofbox, electfham, electfcim]
allcharacters = [aether, amber, lisa, kaeya, xiangling, bennett, noelle, xingqiu, diona, zhongli, eula, venti, baal]

feedbacks = []

items = [testitem]