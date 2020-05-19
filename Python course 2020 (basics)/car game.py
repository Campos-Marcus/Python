word = ''
started = False


while True:
    word = str(input('>').lower())
    if word == "start" and (started == False):
        started = True
        print("the game has started")
    elif word == "stop" and (started == True):
        started = False
        print('the game has stopped')
    elif word == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit 
              """)
    elif word == "quit":
        break
    else:
        print("sorry I don't understand what you said")
