# coding=utf-8
import random
HANGMANPICS = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''
    
+---+
|   |
O   |
    |
    |
    |
=========''', '''
    
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
    
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
    
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========''', '''
    
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========''', '''
    
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========''']
words = {"Animais": "formiga elefante girafa morcego urso besouro camelo gato cobra águia coiote corvo veado cachorro burro pato falcão vespa raposa sapo cabra ganso gavião leão lagarto llama macaco alce rato mula coruja panda papagaio pombo python coelho carneiro rato rinoceronte salmão leão-marinho tubarão ovelha preguiça serpente aranha cisne tigre teru tartaruga baleia lobo zebra".split(),
         "Frutas": "maça pera abacaxi melancia laranja uva pessego".split(),
         "Estados Brasileiros": "acre alagoas amapa amazonas bahia ceara goias maranhao matogrosso para paraiba parana pernambuco piaui rondonia roraima santacatarina saopaulo sergipe tocantins".split()}

def getrandomword(Dict):
    key=random.choice(list(Dict.keys()))
    index=random.randint(0, len(Dict[key])-1)
    return words[key][index], key

def getguess(alreadyguessed):
    while True:
        guess=str(input("Take a guess, stranger")).lower()
        if len(guess) != 1:
            print ("Please, type only one letter!")
        elif guess not in 'abcdefghijklmnopqrstuvxzwxãõâêîôûáéíóú':
            print ("Please, type a LETTER!")
        elif guess in alreadyguessed:
            print ("You already typed this letter!")
        else:
            return guess

def showboard(secretword, HANGMANPICS, missedletters, correctletters):
    blank="_"*len(secretword)
    print(HANGMANPICS[len(missedletters)])
    print ("You missed these letters: ", missedletters)
    print("The class of the secret word is: ", secretkey)
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blank=blank[:i]+secretword[i]+blank[i+1:]
    for letter in blank:
        print (letter, end='')
    print ()

def playagain():
    return input("Do you want to play again?").lower().startswith("y")
        
print ("H A N G M A N ")
correctletters=''
missedletters=''
gameisdone=False
secretword, secretkey=getrandomword(words)

while "Karollinne" != "Kevin":
    showboard(secretword, HANGMANPICS, missedletters, correctletters)
    guess=getguess(missedletters + correctletters)
    if guess in secretword:
        correctletters=correctletters+guess
        won=True
        #Check if player has won
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                won=False
                break
        if won:
            print ("Kudos, you've WON!The word was ", secretword)
            gameisdone=True
    if guess not in secretword:
         missedletters=missedletters+guess
         print ("Too bad, that letter isn't in the secret word")
         #Check if the player has lost
         if len(missedletters)==len(HANGMANPICS)-1:
             showboard(secretword, HANGMANPICS, missedletters, correctletters)
             print ("You've lost! The secret word was ", secretword)
             gameisdone=True
    if gameisdone==True:
        if playagain():
             missedletters=''
             correctletters=''
             gameisdone=False
             secretword=getrandomword(words)
        else:
            print ("Goodbye, stranger!")
            break
         
         
                
        


        
    
          



    

























    
