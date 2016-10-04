import random
import sys
maxchests=3

def showinstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.

To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Press enter to continue...''')
    input()
    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):

    22222
    c   2
    2 d 2
    2   2
    22222

The point where the device was dropped will be marked with a 2.
The treasure chests don’t move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O
If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.
When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.
Press enter to continue...''')
    input()
    print()

def createboard():
    board=[]
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==1:
                board[x].append('~')
            else:
                board[x].append('`')
    return board
    
def iterateboard(board, row):
    boardrow=''
    for x in range(60):
        boardrow+=board[x][row]
    return boardrow
    
def printboard(board):
    firstl=''
    for f in range(1, 6):
        firstl+=(" "*9+str(f))
    secondl=' '*3+('123456789'*7)
    print (firstl)
    print (secondl)
    for g in range(15):
        if g<10:
            extraspace=' '
        else:
            extraspace=''
        print (extraspace, g, iterateboard(board, g), g)
    print ()
    print (secondl)
    print (firstl)
    
def randomchest():
    chests=[]
    for i in range(maxchests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])       
    return chests
    
def validmove(x, y):
    return x<=59 and x>=0 and y<=14 and y>=0
    
def getmove():
    while True:
        move=''
        move=str(input('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)'))
        if move.lower()=="quit":
            print ("Goodbye, stranger!")            
            sys.exit()
        move=move.split()
        if len(move)==2 and move[0].isdigit and move[1].isdigit() and validmove((int(move[0])), (int(move[1]))):
            return [int(move[0]), int(move[1])]
        else:
            print ("Please, type a number, a space, then another number!")

def gethint(board, x, y, chests):
    smallest=2000000000
    for cx, cy in chests:
        if abs(cx-x)>abs(cy-y):
            distance=abs(cx-x)
        else:
            distance=abs(cy-y)
        if distance<smallest:
            smallest=distance
        if smallest==0:
            board[x][y]="X"
            chests.remove([x, y])
            return "KUDOS, you've found a secret treasure!"
        if smallest<10:
            board[x][y]=str(smallest)
            return "Your sonar found a treasure %s meters away" %(smallest)
        if smallest>10:
            board[x][y]="O"
            return "Your sonar did not found anything"

def playagain():
    print ("Do you want to play again?")
    return input().lower().startswith('y')
            
print ("SONAR!")
print ()
print ("Would you like to view further instructions?")
if input().lower().startswith('y'):
    showinstructions()
sonars=16
gameboard=createboard()
gamechests=randomchest()
printboard(gameboard)
history=[]

while True:
    if sonars>1:
        extraSsonar="s"
    else:
        extraSsonar=''
    if len(gamechests)>1:
        extraSchest="s"
    else:
        extraSchest=''
    print ("You have %s sonar%s left, and %s secret chest%s remaining." %(sonars, extraSsonar, len(gamechests), extraSchest))
    x, y=getmove()
    history.append([x, y])
    hint=gethint(gameboard, x, y, gamechests)
    print (hint)
    printboard(gameboard)
    sonars-=1
    if sonars==0:
        print ("Too bad, you've ran out of sonars.")
        if playagain():
            sonars=16
            gameboard=createboard()
            gamechests=randomchest()
            printboard(gameboard)
            history=[]
        else:
            print ("Goodbye, stranger!")
            sys.exit()
    if len(gamechests)==0:
        print ("KUDOS, you've found all the secret chests!")
        if playagain():
            sonars=16
            gameboard=createboard()
            gamechests=randomchest()
            printboard(gameboard)
            history=[]
        else:
            print ("Goodbye, stranger!")
            sys.exit()
    





























