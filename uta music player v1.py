import time
import webbrowser
import pyaudio
import wave
from playsound import playsound

def everything():
    print("lyric loader 1.1.8")
    time.sleep(1)
    print('loading database.....\n')
    time.sleep(1)
    song =input('''select the song you need\n
clarie-backyard boy = "A"
clarie-hotel = "B"\n
press the letter beside the song name on your keyboard to choose
''')
    if song == 'a':
        song_a()
        

    elif song == 'A':
        song_a()
        
    time.sleep(2)

    exi = input('''do you want to play another song or exit?
press "y" to continue
press "x" to exit
''')
    if exi == "y":
        print("okie : )\n")
        everything()
    elif exi == "Y":
        print("okie : )\n")
        everything()
    elif exi =="x":
        print("cya later")
        exit()
    else:
        print("invalid option")
        stop()

def stop():
    exi = input('''do you want to play another song or exit?
press "y" to continue
press "x" to exit''')
    if exi == "y":
        print("okie : )\n")
        everything()
    elif exi == "Y":
        print("okie : )\n")
        everything()
    elif exi =="x":
        print("cya later")
        exit()
    else:
        print("invalid option")
        stop()






















def song_a():
    playsound('C:/Users/mrmak/Downloads/Claire Rosinkranz - BackyardBoy.mp3')
    #webbrowser.open('C:/Users/mrmak/Music/chill/Claire Rosinkranz - Backyard Boy.m4a')
    print('the song will start now')
    time.sleep(9.2)
    print('five')
    time.sleep(0.5)
    print('six')
    time.sleep(0.5)
    print('seven')
    time.sleep(0.5)
    print('eight')
    time.sleep(0.5)
    print('dance with me in my backyard boy')
    time.sleep(2.6)
    print('looking super fine on your corduroy')
    time.sleep(3.5)
    print('drive me by the block')
    time.sleep(1.2)
    print('we can go in a loop')
    time.sleep(1.2)
    print('And we ll turn the volume up')
    time.sleep(2)
    print('On some good boy band tunes\n')
    time.sleep(2)
    print('love I can feel your eyes stare')
    time.sleep(2)
    print('And Im not gonna lie')
    time.sleep(2)
    print('I get a little bit scared')
    time.sleep(2)
    print('My heart is on wings')
    time.sleep(2)
    print('Im living in dreams')
    time.sleep(2)
    print('And at the top of our lungs we sing\n')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da\n')
    time.sleep(2)
    print('Everything is perfect\n')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(3)
    print('Da da da da da da\n')
    time.sleep(2)
    print('All our words were worth it\n')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da\n')
    time.sleep(3)
    print('Dancing around like a clown at the circus\n')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da\n')
    time.sleep(2)
    print('Backyard boy you make me nervous\n')
    time.sleep(4)
    print('Dance with me in my backyard, boy')
    time.sleep(2.6)
    print('Looking super fine in your corduroy (five, six, seven, eight)')
    time.sleep(3.5)
    print('Roll the windows down')
    time.sleep(2)
    print('Let the bass drop low')
    time.sleep(3)
    print('And everybodys talking')
    time.sleep(2)
    print('But I dont wanna know\n')
    time.sleep(3)
    print('Feel the fresh air')
    time.sleep(3)
    print('I can feel your eyes stare')
    time.sleep(1)
    print('And Im not gonna lie')
    time.sleep(1)
    print('I get a little bit scared')
    time.sleep(2)
    print('My heart is on wings')
    time.sleep(1)
    print('Im living in dreams')
    time.sleep(2)
    print('And at the top of our lungs we sing\n')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(3)
    print('Everything is perfect')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(1)
    print('All our words were worth it')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(3)
    print('Dancing around like a clown at the circus')
    time.sleep(2)
    print('Da da da da da da')
    time.sleep(3)
    print('Da da da da da da')
    time.sleep(2)
    print('Backyard boy, you make me nervous\n')
    time.sleep(8)
    print('Right now?')





everything()



