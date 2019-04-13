import pyautogui
import pyscreeze
import time

from PIL import ImageOps, ImageGrab

left = 'left'
right = 'right'
down = 'down'
up = 'up'
currentGrid = [0, 0,
               0, 0]

def getGrid():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)

    for index, check in enumerate(BattleOptions.BattleOptionsArray):
        pixel = grayImage.getpixel(check)
        pos = BattleOptionsColors.BattleOptionsColorsArray.index(pixel)
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2, pos)


class BattleOptionsColors:
    RunRed = 40
    RunGrey = 136
    RunBlu = 144
    FightRed = 57
    FightGrey = 193
    FightYellow = 223
    BagRed = 42
    BagGrey = 142
    BagYellow = 200
    ChoosePokeRed = 32#battle phase started.
    ChoosePokeGrey = 110
    ChoosePokeRedReady = 76#not at start of battle
    ProWindowIconColor = 132

    BattleOptionsColorsArray = [RunRed, RunGrey, RunBlu, FightRed, FightGrey, FightYellow, BagRed, BagGrey, BagYellow,ChoosePokeRed, ChoosePokeGrey, ChoosePokeRedReady]


class BattleOptions:
    isProWindowOpen = (462, 149) #this is the pokeball at top right of PRO Window
    BattleRun = (1305, 740)
    BattleFight = (1200, 666)
    BattleBag = (1201, 741)
    BattleChoosePoke = (1286, 656)

    BattleOptionsArray = [BattleRun, BattleFight, BattleBag, BattleChoosePoke]


def timer():
    for i in (range(4))[:: -1]:
        print(i + 1)
        time.sleep(1)
    print("\n")


def ColorFromMouse():
    mousex, mousey = pyautogui.position()
    color = pyscreeze.pixel(mousex, mousey)
    return color


def keypress(key):
    pyautogui.keyDown(key)
    time.sleep(.5)
    pyautogui.keyUp(key)


def walkleft():
    walk = 15
    i = 0
    while i < walk:
        keypress(left)
        i += 1


def walkright():
    walk = 15
    i = 0
    while i < walk:
        keypress(right)
        i += 1


def ColorOfAllInBattlescene():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    for check in BattleOptions.BattleOptionsArray:
        pixel = grayImage.getpixel(check)
        print(pixel)


def isWildPokemon():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    pixel = grayImage.getpixel(BattleOptions.BattleRun)
    print(pixel)
    if pixel != BattleOptionsColors.RunGrey:
        print("not in battle")
        return False
    return True


def PROWindowLocation():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    pixel = grayImage.getpixel(BattleOptions.isProWindowOpen)
    print(pixel)
    if pixel == BattleOptionsColors.ProWindowIconColor:
        print("PRO Window is open. coords: 462, 149\n")
        return True
    return False

def main():
    timer()
    if PROWindowLocation() == False:
        print("ProWindow not at same location. Icon must be visible and same location at all times")
        return 0

    if not isWildPokemon():
        walkright()
        walkleft()
    #checks prowindow location
   # print("mouse reading")
    #print(pyautogui.displayMousePosition()) #hovers over mouse to determine rgb
    #ColorFromMouse()


main()
