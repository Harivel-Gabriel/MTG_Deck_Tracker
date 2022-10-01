from mtgsdk import Card


#cards = Card.where(name='Arcángel Avacyn').where(language='spanish').all()
#print(cards[0].name)


def getCardInfo(nom :str):
    cards = Card.where(name=nom).where(language='french').all()[0]
    return ";" + cards.name + ";" + str(cards.colors) + ";" + str(int(cards.cmc))

    