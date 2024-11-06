import smartcard.Exceptions
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString

cardtype = AnyCardType()

cardrequest = CardRequest(timeout=1, cardType=cardtype)

try:
    cardservice = cardrequest.waitforcard()
except smartcard.Exceptions.CardRequestTimeoutException:
    print("no card detected!")
else:
    cardservice.connection.connect()
    print("card's ATR is:" + toHexString(cardservice.connection.getATR()))
