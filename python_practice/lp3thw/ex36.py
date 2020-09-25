def intro_to_game():
    print("Some of the information, I provide here, might be useful. Read them.")
    print("Press ENTER to continue...")
    input("")
    print("""1. You got 3 lives.
2. Each mistake you make cost a life.
3. Be careful! The game will be encoded after you play it once and you won't
    be able to access it after your lives are over.
4. I have't any more information.""")
    print("\nPress ENTER to start GAME...")
    input("")

def hall_room():
    print("You enter THE HOUSE and now you are in the HALL ROOM.")
    hall_hint1 = "Monalisa Picture"
    hall_hint2 = "A picture of Krishna eating Makkhan"
    hall_hint3 = "A television with a still picture of Krishna in the movie 'Mahabharata'"
    hall_hint4 = "A certificate of someone's achievement in counting similar pictures."
    hall_hint5 = "Others are just furnitures and some regular stuff. Don't think there might be a clue there."
    hall_hint6 = "There are three doors leading to three different rooms: Room1, Room2, Room3"
    hall_hints = [hall_hint1, hall_hint2, hall_hint3, hall_hint4, hall_hint5, hall_hint6]

    hall_hints_call(hall_hints)

    room_choose()

def room_1():
    print()

def room_2():
    print("You pushed the door that leads you here: Room2")
    print("Press ENTER to continue...")
    input()

    print("I'll give you some info about ROOM2.")
    print("There you go...")
    room2_hint1 = "Room2 seems to be a bedroom."
    room2_hint2 = "The bedsheets are in a mess."
    room2_hint3 = "There is a tea-table and a lamp which is on."
    room2_hint4 = "There is a link door here which will lead you to Room2"
    room2_hint5 = "There is another door here with a writing saying 'ROOM LOCKED!'. The key might be there somewhere in the house."

    room2_hints = [room2_hint1, room2_hint2, room2_hint3, room2_hint4, room2_hint5]

    j = 1
    for i in room2_hints:
        print(f"{j}. {i}")
        j += 1
        input()

    print("Choose what would you like to do?")
    print("""Choices:
1. Search for key in the room.
2. Enter Room3 to search for the key.
""")


def room_3():
    print()

def hall_hints_call(hall_hints):
    print("Would you like some hints about the HALL ROOM?(y,n)")
    choice = input()

    if choice == 'y':
        j = 1
        print("There you go:")
        for i in hall_hints:
            print(j,".",i, end='')
            j += 1
            input()
    elif choice == 'n':
        print("Goddamn MF! Why are you here then? Can't you \"STRAIGHT FORWARDLY\" say 'y'?")
        print("I am repeating the question!")
        return hall_hints_call(hall_hints)
    else:
        print("You Fu*K! Don't you have eyes to read options?")
        print("I repeat the question!")
        return hall_hints_call(hall_hints)

def room_choose():
    print("\n")
    print("Now use your investigator mind and choose carefully which room(1, 2, 3), would you like to enter?")
    choice = input()

    if choice == "1":
        room_1()
    elif choice == "2":
        room_2()
    elif choice == "3":
        room_3()
    else:
        print("Fu*k! You really got no sense. Could you at least make a right choice?")
        print("I'll again ask!")
        return room_choose()

intro_to_game()
hall_room()
