import random

def choose():
    words=['rainbow','computer','happiness','india','knowledge',]
    pick=random.choice(words)
    return pick

def jumble(words):
    jumble="".join(random.sample(words,len(words)))
    return jumble

def thanks(p1,p2,point1,point2):
    print(p1,'Your Score: ',point1)
    print(p2,'Your Score: ',point2)
    print('Thanks for playing :)')

def play():
    p1=input('Player1 Name: ')
    p2=input('Player2 Name: ')
    point1=0
    point2=0
    turn=0
    while(1):
        #computer' Task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player 1:
        if turn%2==0:
            print(p1,'Your Turn.')
            ans=input('What is the correct WORD?: ')
            if ans==picked_word:
                point1=point1+1
                print('Correct! Your Score is: ',point1)
            else:
                print('Game Over, Correct Answer: ',picked_word)
            c=int(input('Press 1 to Continue or Anyother to Quit: '))
            if c==0:
                thanks(p1,p2,point1,point2)
                break
        #player 2:
        else:
            print(p2,'Your Turn.')
            ans=input('What is the correct WORD?: ')
            if ans==picked_word:
                point2=point2+1
                print('Correct! Your Score is: ',point2)
            else:
                print('Game Over, Correct Answer: ',picked_word)
            c=int(input('Press 1 to Continue or Anyother to Quit: '))
            if c==0:
                thanks(p1,p2,point1,point2)
                break
        turn=turn+1
play()