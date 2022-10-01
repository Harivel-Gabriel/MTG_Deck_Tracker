import numpy as np
from mtgsdk import Card

#cardNotFound = Card()
#cardNotFound.name, cardNotFound.cmc, cardNotFound.colors = "404 Not found", "404 Not found", 404

def Separation(X :str):
#   Place un ";" entre le nombre de cartes et son nom en français 
    text=list(X)
    text.pop()
    text.pop()
    for ii in range(len(text)):
        if text[ii].isnumeric():
            if text[ii + 1].isnumeric():
                text[ii + 2] = ";"
                return ''.join(text)
            else:
                text[ii + 1] = ";"
                return ''.join(text)

def getCardInfos(nom :str):
#   Récupère les informations de la carte à partir de son nom fr via le MTG SDK
    cards = Card.where(name=nom).where(language='french').all()
    if len(cards) == 0:
        print("CardNotFound")
        return "error"
    else:
        return cards[0]


    #return ";" + cards.name + ";" + str(cards.colors) + ";" + str(int(cards.cmc))

def getSourceName(X):
#   Récupère le nom de la carte en français dans le fichier source, après avoir séparé le nom du nombre de cartes par ";"
    L=X.split(';')
    return L[1]

###################################################################################        
#  __  __          _____ _   _ 
# |  \/  |   /\   |_   _| \ | |
# | \  / |  /  \    | | |  \| |
# | |\/| | / /\ \   | | | . ` |
# | |  | |/ ____ \ _| |_| |\  |
# |_|  |_/_/    \_\_____|_| \_|
###################################################################################                                 

file = open("Ameliorations_dechainees.csv", "r")
#file = open("test.csv", "r")
replacement = ""
ii=1

for line in file:
    print("Traitement n°" + str(ii) + "/74")
    changes = Separation(line)
    currentCard = getCardInfos(getSourceName(changes.strip()))
    if currentCard != "error":
        replacement = replacement + changes + ";" + ''.join(currentCard.colors) + ";" + str(int(currentCard.cmc)) + "\n"
    else:
        replacement= replacement + "error 404 : Card not found \n"
    ii=ii+1
file.close()

#print(replacement)

# opening the file in write mode
fout = open("Ameliorations_dechainees.csv", "w")
#fout = open("test.csv", "w")
fout.write(replacement)
fout.close()
