room = 'starting'
game_running = True
import time

while game_running:
  if room == 'starting':
    print("You find yourself in a big room with 3 doors one is red, on yellow, one door with a lock")
    room = input("red, yellow, lock?")

    while room == "red":
        print("You now find yourself in a red room")
        time.sleep (2)
        print("On the wall there are two buttons")
        time.sleep (2)
        print("the red button is labeled '1'")
        time.sleep (2)
        print("the blue button is labeled '3'")
        button = input("red,blue or leave?")
        if button.lower() == "leave":
            room = 'starting'
        elif button == "red":
            print("A screen lights up showing the number '6'")
            print("You feel like you should remember this button")
            time.sleep (3)
            room = "red"
        elif button == "blue":
            print("A screen lights up showing the number '8'")
            print("You really feel this number may be important")
            time.sleep (3)
            room = "red"
        else:
            print("invalid response")
            room = "red"

    while room == "yellow":
        print("You are in a bright yellow room with a very very bright light") 
        print("It's too hard to see in this room")
        uhm = input("Feel around (1), or leave?")
        if uhm == "leave":
            room = 'starting'
        elif uhm == "1":
            print("You find a button and press it.")
            print("a speaker turns on")
            print(" 'What hase four legs when it's born, two in the middle of its life and three at the end' ")
            answer = input("Answer to the ridle:")
        
            if answer == "human" or "people" or "i" or "me" or "an octopus".lower():
                print("'You are correct!'")
                time.sleep (1)
                print("A room opens and inside you see a wall:")
                print("    THE")
                print("       2nd                    IS")
                print("         NUMBER                  9")
                time.sleep (1)
                print("I swear to god if it isn't obvious enough.")
                time.sleep (3)
                print("You return to the yellow room and the light hase been turned off")
                time.sleep (1)
                if room == "yellow":
                    print("You see a screen with a math puzzle on the wall and an open door")
                    answer = input("leave, puzzle, door:")
                    if answer == "leave":
                        room = 'starting'
                    elif answer == "door":
                        room = "small room"
                    elif answer == "puzzle":
                        print("fourth number = 4+6/2-2-1/1")
                        time.sleep (2)
                        room = 'starting'
        else:
            print("invalid response")
            room = "yellow"
    while room == "lock":
        print("On the door is a lock that needs a four number code")
        code = input("What's the code?")
        if code == "6984":
            print("You win and i love you")
            time.sleep (1)
            print("I shall give you an octopus in thought")
            room = 'win'
        else:
            print("Nope go find the numbers in the other rooms")
            time.sleep (1)
            print("If the math puzzle is too hard type 1")
            answer = input("1 or leave?")
            if answer == "1":
                print("The answer is 4 dumbass")
                time.sleep (2)
                room = 'starting'
            if answer == "leave":
                room = 'starting'
    if room == 'win':
        print()
        answer = input("Press 1 to start again.")
        if answer == "1":
            room = 'starting'
    else:
        print("invalid respons")
        room = 'starting'
                        
                    


            


    



   


