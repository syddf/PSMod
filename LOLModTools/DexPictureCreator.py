from PIL import Image, ImageDraw, ImageFont
import os
import glob
import shutil
import json

abilityDic = {
    'CuteCharm' : '迷人之躯',
    'SuperLuck' : '超幸运',
    'Protean' : '变换自如',
    'Technician' : '技术高手',
    'DarkAura' : '暗黑气场',
    'Levitate' : '飘浮',
    'Simple' : '单纯',
    'Illuminate': '发光',
    'Adaptability' : '适应力',
    'InnerFocus' : '精神力',
    'BattleArmor' : '战斗盔甲',
    'SteelySpirit' : '钢之意志',
    'MagicGuard' : '魔法防守',
    'Regenerator' : '再生力',
    'Magician' : '魔术师',
    'Disguise' : '画皮',
    'Illusion' : '幻觉',
    'PoisonTouch' : '毒手',
    'BigPecks' : '健壮胸肌'
}

movDic = {
    'dazzlinggleam' : '魔法闪耀',
    'drainingkiss' : '吸取之吻',
    'moonblast' : '月亮之力',
    'spiritbreak' : '灵魂冲击',
    'craftyshield' : '戏法防守',
    'mistyterrain' : '薄雾场地',
    'mistyexplosion' : '薄雾炸裂',
    'protect' : '守住',
    'psychic' : '精神强念',
    'charm' : '撒娇',
    'lightscreen' : '光墙',
    'reflect' : '反射壁',
    'icebeam' : '冰冻光线',
    'thunderbolt' : '十万伏特',
    'drainpunch' : '吸取拳',
    'faketears' : '假哭',
    'shadowball' : '暗影球',
    'nastyplot' : '诡计',
    'disable' : '定身法',
    'aurasphere' : '波导弹',
    'flamecharge' : '蓄能焰袭',
    'fierydance' : '火之舞',
    'mysticalfire' : '魔法火焰',
    'suckerpunch' : '突袭',
    'dig' : '挖洞',
    'earthpower' : '大地之力',
    'rototiller' : '耕地',
    'highhorsepower' : '十万马力',
    'pursuit' : '追打',
    'taunt' : '挑衅',
    'knockoff' : '拍落',
    'throatchop' : '深渊突刺',
    'payback' : '以牙还牙',
    'quickattack' : '电光一闪',
    'doubleteam' : '影子分身',
    'smokescreen' : '烟幕',
    'haze' : '黑雾',
    'aerialace' : '燕返',
    'leafblade' : '叶刃',
    'xscissor' : '十字剪',
    'clearsmog' : '清除之烟',
    'highjumpkick' : '飞膝踢',
    'grassyterrain' : '青草场地',
    'uturn' : '急速折返',
    'acrobatics' : '杂技',
    'agility' : '高速移动',
    'appleacid' : '苹果酸',
    'darkpulse' : '恶之波动',
    'nightdaze' : '暗黑爆破',
    'futuresight' : '预知未来',
    'extrasensory' : '神通力',
    'calmmind' : '冥想',
    'psychicterrain' : '精神场地',
    'speedswap' : '速度互换',
    'skillswap' : '特性互换',
    'imprison' : '封印',
    'painsplit' : '分担痛楚',
    'psybeam' : '幻象光线',
    'hyperbeam' : '破坏光线',
    'aurorabeam' : '极光束',
    'solarbeam' : '日光束',
    'confuseray' : '奇异之光',
    'lusterpurge' : '洁净光芒',
    'signalbeam' : '信号光束',
    'mirrorshot' : '镜光射击',
    'flashcannon' : '加农光炮',
    'chargebeam' : '充电光束',
    'simplebeam' : '单纯光束',
    'auroraveil' : '极光幕',
    'moongeistbeam' : '暗影之光',
    'steelbeam' : '铁蹄光线',
    'partingshot' : '抛下狠话',
    'foulplay' : '欺诈',
    'rest' : '睡觉',
    'trick' : '戏法',
    'expandingforce' : '广域战力',
    'psyshock' : '精神冲击',
    'coaching' : '指导',
    'finalgambit' : '搏命',
    'closecombat' : '近身战',
    'machpunch' : '音速拳',
    'bulkup' : '健美',
    'mimic' : '模仿',
    'copycat' : '仿效',
    'rockslide' : '岩崩',
    'sandstorm' : '沙暴',
    'rocktomb' : '岩石封锁',
    'stoneedge' : '尖石攻击',
    'stealthrock' : '隐形岩',
    'wideguard' : '广域防守',
    'irondefense' : '铁壁',
    'sunsteelstrike' : '流星闪冲',
    'metalburst' : '金属爆炸',
    'ironhead' : '铁头',
    'bodypress' : '扑击',
    'dragondance' : '龙之舞',
    'breakingswipe' : '广域破坏',
    'takedown' : '猛撞',
    'doubleedge' : '舍身冲撞',
    'flipturn' : '快速折返',
    'willowisp' : '磷火',
    'firespin' : '火焰旋涡',
    'thunderwave' : '电磁波',
    'toxic' : '剧毒',
    'recover' : '自我再生',
    'swagger' : '虚张声势',
    'followme' : '看我嘛',
    'scaryface' : '可怕面孔',
    'burningjealousy' : '妒火',
    'fireblast' : '大字爆炎',
    'flameburst' : '烈焰溅射',
    'flareblitz' : '闪焰冲锋',
    'blazekick' : '火焰踢',
    'sunnyday' : '大晴天',
    'superpower' : '蛮力',
    'brickbreak' : '劈瓦',
    'noretreat' : '背水一战',
    'crosspoison' : '十字毒刃',
    'slash' : '劈开',
    'substitute' : '替身',
    'dualchop' : '二连劈',
    'dragonclaw' : '龙爪',
    '' : '',

}

directory = os.getcwd()
PSServerRootPath = 'D:\\Code\\PSServer'
PSClientRootPath = 'D:\\Code\\PSClient'
LoLPokemonDataRootPath = directory + '\\LoLPokemonData'

typesImg = Image.open(directory + '\\Types.png')
typeImgDic = {
    'Normal' : typesImg.crop((0, 9, 115, 38)),
    'Fire' : typesImg.crop((0, 9 + 38 * 1, 115, 38 + 38 * 1)),
    'Water' : typesImg.crop((0, 9 + 38 * 2, 115, 38 + 38 * 2)),
    'Electric' : typesImg.crop((0, 9 + 38 * 3, 115, 38 + 38 * 3)),
    'Grass' : typesImg.crop((0, 9 + 38 * 4, 115, 38 + 38 * 4)),
    'Ice' : typesImg.crop((0, 9 + 38 * 5, 115, 38 + 38 * 5)),
    'Fighting' : typesImg.crop((0, 9 + 38 * 6, 115, 38 + 38 * 6)),
    'Poison' : typesImg.crop((0, 9 + 38 * 7, 115, 38 + 38 * 7)),
    'Ground' : typesImg.crop((0, 9 + 38 * 8, 115, 38 + 38 * 8)),

    'Flying' : typesImg.crop((122, 9, 237, 38)),
    'Psychic' : typesImg.crop((122, 9 + 38 * 1, 237, 38 + 38 * 1)),
    'Bug' : typesImg.crop((122, 9 + 38 * 2, 237, 38 + 38 * 2)),
    'Rock' : typesImg.crop((122, 9 + 38 * 3, 237, 38 + 38 * 3)),
    'Ghost' : typesImg.crop((122, 9 + 38 * 4, 237, 38 + 38 * 4)),
    'Dragon' : typesImg.crop((122, 9 + 38 * 5, 237, 38 + 38 * 5)),
    'Dark' : typesImg.crop((122, 9 + 38 * 6, 237, 38 + 38 * 6)),
    'Steel' : typesImg.crop((122, 9 + 38 * 7, 237, 38 + 38 * 7)),
    'Fairy' : typesImg.crop((122, 9 + 38 * 8, 237, 38 + 38 * 8)),
}

moveTypeDic = {

}

with open(PSServerRootPath + '\\data\\moves.ts', 'r') as f:
    moves = f.read()

for move, moveCN in movDic.items():
    moveInd = moves.find('\t' + move + ': {')
    typeInd = moves.find("type: \"", moveInd)
    typeValueInd = moves.find("\"", typeInd)
    typeValueEndInd = moves.find("\"", typeValueInd + 1)
    moveTypeDic[move] = moves[typeValueInd + 1:typeValueEndInd]

def CreatePkmDex(name):
    with open(PSServerRootPath + '\\data\\pokedex.ts', 'r') as f:
        dexlines = f.readlines()
    with open(PSServerRootPath + '\\data\\learnsets.ts', 'r') as f:
        movlines = f.readlines()
   
    findPKM = 0
    count = 0

    pkmName = ''
    pkmType0 = ''
    pkmType1 = ''
    pkmHP = ''
    pkmATK = ''
    pkmDEF = ''
    pkmSATK = ''
    pkmSDEF = ''
    pkmSPEED = ''
    pkmAbility = []
    pkmMov = []

    for line in movlines:
        if ('\t' + name + ':') in line:
            findPKM = 1
        if '{' in line:
            if(findPKM):
                count += 1
        if '}' in line:
            if(findPKM):
                count -= 1
                if(count == 0):
                    break
        if findPKM == 1:
            result = line.replace('\r','').replace('\t','').replace('\n','')[:-1].split(":")
            if(movDic.get(result[0]) is None):
                continue
            pkmMov.append(result[0])

    findPKM = 0
    count = 0
    for line in dexlines:
        if ('\t' + name + ':') in line:
            findPKM = 1
        if '{' in line:
            if(findPKM):
                count += 1
        if '}' in line:
            if(findPKM):
                count -= 1
                if(count == 0):
                    break
        if findPKM == 1:
            result = line.replace('\r','').replace('\t','').replace('\n','')[:-1].split(":")
            if(result[0] == 'name'):
                pkmName = result[1].replace(' ','')
            if(result[0] == 'types'):
                types = result[1].replace('[','').replace(']','').replace('"', '').split(",")
                pkmType0 = types[0].replace(' ','')
                if len(types) > 1:
                    pkmType1 = types[1].replace(' ','')
            if(result[0] == 'baseStats'):
                result = line.replace(' ','').replace('\r','').replace('\t','').replace('\n','').replace('{','').replace('}','')[:-1].replace(':',',').split(",")
                stats = result
                i = 0                
                while i < len(stats):
                    if stats[i] == 'hp':
                        pkmHP = stats[i+1]
                    if stats[i] == 'atk':
                        pkmATK = stats[i+1]
                    if stats[i] == 'def':
                        pkmDEF = stats[i+1]
                    if stats[i] == 'spa':
                        pkmSATK = stats[i+1]
                    if stats[i] == 'spd':
                        pkmSDEF = stats[i+1]
                    if stats[i] == 'spe':
                        pkmSPEED = stats[i+1]
                    i += 1
            if(result[0] == 'abilities'):
                result = line.replace(' ','').replace('"','').replace('\r','').replace('\t','').replace('\n','').replace('{','').replace('}','')[:-1].replace(':',',').split(",")
                print(result)
                i = 0
                while i < len(result):
                    if result[i] == '0':
                        pkmAbility.append(result[i+1])
                    if result[i] == '1':
                        pkmAbility.append(result[i+1])
                    if result[i] == 'H':
                        pkmAbility.append(result[i+1])
                    i += 1
    image = Image.open(directory + '\\DexBackground.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('C:\\WINDOWS\\FONTS\\msyh.ttc', size=20)
    font2 = ImageFont.truetype('C:\\WINDOWS\\FONTS\\msyh.ttc', size=15)
    avatorImg = Image.open(LoLPokemonDataRootPath + '\\' + name + '\\' + name + '.png')
    abilityString = abilityDic[pkmAbility[0]]
    for ability in pkmAbility:
        if(abilityDic[ability] != abilityString):
            abilityString = abilityString + '/' + abilityDic[ability]
    draw.text((310, 80), abilityString, font=font, fill=(0, 0, 0))
    draw.text((350, 118), pkmHP, font=font2, fill=(0, 0, 0))
    draw.text((350, 137), pkmSPEED, font=font2, fill=(0, 0, 0))
    draw.text((438, 118), pkmATK, font=font2, fill=(0, 0, 0))
    draw.text((438, 137), pkmDEF, font=font2, fill=(0, 0, 0))
    draw.text((530, 118), pkmSATK, font=font2, fill=(0, 0, 0))
    draw.text((530, 137), pkmSDEF, font=font2, fill=(0, 0, 0))

    movIndx = 0
    movY = 220
    for mov in pkmMov:
        draw.text((70, movY + movIndx * 30), movDic[mov] + '(' + mov + ')', font=font, fill=(0, 0, 0))
        image.paste(typeImgDic[moveTypeDic[mov]], (430, movY + movIndx * 30), typeImgDic[moveTypeDic[mov]])
        movIndx += 1

    position = (100, 200)
    leftUpPosition = (55, 25)
    rightendPosition = (195, 165)
    avatorSize = avatorImg.size

    avatorX = ((rightendPosition[0] - leftUpPosition[0]) - avatorSize[0]) / 2 + leftUpPosition[0]
    avatorY = ((rightendPosition[1] - leftUpPosition[1]) - avatorSize[1]) / 2 + leftUpPosition[1]
    avatorPos = (int(avatorX), int(avatorY))
    image.paste(avatorImg, avatorPos, avatorImg)
    image.paste(typeImgDic[pkmType0], (310, 35), typeImgDic[pkmType0])
    if(pkmType1 != ''):
        image.paste(typeImgDic[pkmType1], (430, 35), typeImgDic[pkmType1])
    image.save(directory + '\\'  + name + '.png')


def traverse_files(folder_path, dataFileName):
    fileList = []
    folderList = []
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isdir(file_path):
            folderList.append(file_name)
            subfileList, subfolderList = traverse_files(file_path, dataFileName)
            fileList = fileList + subfileList
        else:  
            if(file_name == dataFileName):
                fileList.append(file_path)
    return fileList, folderList


fileList, folderList = traverse_files(LoLPokemonDataRootPath, 'DexData.txt')
for folder in folderList:
    CreatePkmDex(folder)