from enum import Enum
import SenseHatGameEngine as shge

class GameState(Enum):
    UNDEFINED = 0
    SHIP_PLACEMENT = 1
    PLAYING = 2
    OVER = 3

class Player(Enum):
    UNDEFINED = 0
    PLAYER1 = 1
    PLAYER2 = 2
    KI = 3


