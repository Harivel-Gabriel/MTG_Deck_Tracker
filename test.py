from mtgsdk import Card


def getCardInfo():
    cards = Card.where(name='Robot-guide de Towashi').where(language='french').all()
    if len(cards) == 0:
        return 0
    else:
        return cards[0]

cardNotFound = Card()
cardNotFound.name="404 Not found"

print(getCardInfo().colors)