from PIL import Image
import os
import glob
import shutil

directory = os.getcwd()

abilityDic = {
    'Cute Charm' : '迷人之躯',
    'Super Luck' : '超幸运'
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
    'aurasphere' : '暗影球',
}