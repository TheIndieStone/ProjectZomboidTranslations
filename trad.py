myst = '''ItemName_IT = {
    ItemName_Base.223Box = "Scatola di munizioni .223",
    ItemName_Base.223Bullets = "Munizioni .223",
    ItemName_Base.223BulletsMold = "Stampo per munizioni .223",
    ItemName_Base.308Box = "Scatola di munizioni .308",
    ItemName_Base.308Bullets = "Munizioni .308",
    ItemName_Base.308BulletsMold = "Stampo per munizioni .308",
    ItemName_Base.9mmBulletsMold = "Stampo per munizioni 9mm",
    ItemName_Base.9mmClip = "Caricatore per 9mm",
    ItemName_Base.Aerosolbomb = "Bomba aerosol",
    ItemName_Base.AerosolbombRemote = "Telecomando per bomba aerosol",
    ItemName_Base.AerosolbombSensorV1 = "Bomba aerosol con sensore",
    ItemName_Base.AerosolbombSensorV2 = "Bomba aerosol con sensore",
    ItemName_Base.AerosolbombSensorV3 = "Bomba aerosol con sensore",
    ItemName_Base.AerosolbombTriggered = "Bomba aerosol con timer",
    ItemName_Base.AlarmClock = "Sveglia",
    ItemName_Base.WaterBottleEmpty = "Bottiglia vuota",
    ItemName_Base.WaterBottleFull = "Bottiglia d'acqua",
    ItemName_Base.WaterBowl = "Scodella d'acqua",
    ItemName_Base.WaterDish = "Piatto con acqua",
    ItemName_Base.WaterDrop = "Goccia d'acqua",
    ItemName_Base.WaterMug = "Tazza d'acqua",
    ItemName_Base.WaterPopBottle = "Bottiglia d'acqua",
    ItemName_Base.WaterPot = "Pentola con acqua",
'''
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
print(dir_path)
print(cwd)
file = open(r'IT/ItemName_IT.txt', 'r+', encoding='utf8')
for line in file.readlines():
    print(line)
