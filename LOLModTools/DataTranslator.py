from PIL import Image
import os
import glob
import shutil

directory = os.getcwd()

PSServerRootPath = 'D:\\Code\\PSServer'
PSClientRootPath = 'D:\\Code\\PSClient'
LoLPokemonDataRootPath = directory + '\\LoLPokemonData'
LoLDataTag = 'LOLDATA'

def WriteData(path, content):
    contentBegin = 0
    writed = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        i = 0
        while(i < len(lines)):
            if(LoLDataTag in lines[i]):
                if(contentBegin == 1):
                    lines[i] = content + '\n' + lines[i]
                    break
                else:
                    contentBegin = 1
            elif(contentBegin == 1):
                lines[i] = ''
            i+=1
    with open(path, 'w') as f:
        f.writelines(lines)


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



def WriteBasePokeDexData():
    fileList, folderList = traverse_files(LoLPokemonDataRootPath, 'DexData.txt')
    content = ''
    i = 0
    while i < len(fileList):
        with open(fileList[i], 'r') as file:
            content = content + '\n\t' + folderList[i] + ':' + file.read()
        i += 1
    WriteData(PSServerRootPath + '\\data\\pokedex.ts', content)

def WriteBaseLearnSetData():
    fileList, folderList = traverse_files(LoLPokemonDataRootPath, 'LearnSet.txt')
    content = ''
    i = 0
    while i < len(fileList):
        with open(fileList[i], 'r') as file:
           content = content + '\n\t' + folderList[i] + ':' + file.read()
        i += 1
    WriteData(PSServerRootPath + '\\data\\learnsets.ts', content)

def WriteFormatsData():
    baseFormat = '{\n		isNonstandard: "GEN8LOL",\n		tier: "Illegal",\n	},'
    fileList, folderList = traverse_files(LoLPokemonDataRootPath, 'Formats.txt')
    baseContent = ''
    modContent = ''
    i = 0
    while i < len(fileList):
        with open(fileList[i], 'r') as file:
           modContent = modContent + '\n\t' + folderList[i] + ':' + file.read()
           baseContent = baseContent + '\n\t' + folderList[i] + ':' + baseFormat
        i += 1
    WriteData(PSServerRootPath + '\\data\\formats-data.ts', baseContent)
    WriteData(PSServerRootPath + '\\data\\mods\\gen8lol\\formats-data.ts', modContent)
   
def CopySpritesToClient():
    fileList, folderList = traverse_files(LoLPokemonDataRootPath, 'DexData.txt')
    content = ''
    i = 0
    while i < len(folderList):
        pkmName = folderList[i]
        frontAnimFile = LoLPokemonDataRootPath + '\\' + pkmName + '\\' + pkmName + '.gif'
        backAnimFile = LoLPokemonDataRootPath + '\\' + pkmName + '\\' + pkmName + '-back.gif'
        iconFile = LoLPokemonDataRootPath + '\\' + pkmName + '\\' + pkmName + '_icon.png'
        faceFile = LoLPokemonDataRootPath + '\\' + pkmName + '\\' + pkmName + '.png'

        targetFrontAnimFile = PSClientRootPath + '\\play.pokemonshowdown.com\\sprites\\ani\\' + pkmName + '.gif'
        targetBackAnimFile = PSClientRootPath + '\\play.pokemonshowdown.com\\sprites\\ani-back\\' + pkmName + '.gif'
        targetIconFile = PSClientRootPath + '\\play.pokemonshowdown.com\\sprites\\gen5\\' + pkmName + '_icon.png'
        targetFaceFile = PSClientRootPath + '\\play.pokemonshowdown.com\\sprites\\gen5\\' + pkmName + '.png'
        shutil.copy(frontAnimFile, targetFrontAnimFile)
        shutil.copy(backAnimFile, targetBackAnimFile)
        shutil.copy(iconFile, targetIconFile)
        shutil.copy(faceFile, targetFaceFile)
        i += 1


WriteBasePokeDexData()
WriteBaseLearnSetData()
WriteFormatsData()
CopySpritesToClient()