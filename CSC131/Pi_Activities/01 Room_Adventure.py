######################################################################
# Name: Caleb Matherne
# Date: 12/31/2021 - 1/13/2022
# Description: Room Adventure Pi Activity
######################################################################

# ADDED :

# The things I added are descriptions for the grabbables, a use action
# to use grabbables to progress to other rooms, auto generated 
# room descriptions, auto generated user actions, optional custom room 
# descriptions, optional custom use descriptions, room and item
# descriptions that change when the user takes grabbables, an 
# inventory action to examine picked-up items, a npc

######################################################################

# Things I could have done better :

# Made a function in the class to change the description of items 
# and/or grabbables for cleaner code in some places.

# I probably could have used far less if statements through other
# methods for cleaner code, but oh well. It's ugly but it works.

# Think a bit harder on the conclusion to make it more coherent

# Give more attention to the auto generated descriptions, especially
# in rooms 3-5 because lots of the clues are in the details not
# present in the auto generated descriptions.

######################################################################

# TUTORIAL (SPOILERS)
# Grab key, use key, go south, grab book, go north, use book, go east, 
# grab lighter, use torn_book, use lighter, use page, go south, 
# grab 6-pack, use 6-pack, go south. take 6-pack, talk caleb x4, 
# go south.

######################################################################
"""
TO DO
Nothing!
I'm finished! (hopefully)
"""
######################################################################

import random

class Room:
    def __init__ (self, name, rdesc, ruse):
        #room name
        self.name = name
        #room description
        self.rdesc = rdesc
        #room usable items
        self.ruse = ruse
        #exit direction
        self.exits = []
        #exit location (room #)
        self.exitL = []

        self.items = []
        self.idesc = []
        self.grabs = []
        self.gdesc = []
        self.npc = []
        self.npcdialogue = []

#Room Functions
    def addExit(self, exit, room):
        #exit to north, south, east, west
        self.exits.append(exit)
        #leading to room#
        self.exitL.append(room)

    def addItem(self, item, itemdesc):
        self.items.append(item)
        self.idesc.append(itemdesc)

    def addGrab(self, grab, grabdesc):
        self.grabs.append(grab)
        self.gdesc.append(grabdesc)

    def delGrab(self, item):
        self.gdesc.remove(self.gdesc[self.grabs.index(item)])
        self.grabs.remove(item)

    def addNPC(self, name, dialogue):
        self.npc.append(name)
        self.npcdialogue.append(dialogue)



def createRooms():
    global currentRoom

    r1 = Room("Room 1", "You find yourself in a bright room with what seems to be once-was furniture \
scattered about the corners of the room and covered with a blanket of dust. The setting sun's light \
illuminates the wall through an opposing window, catching specs of floating dust falling from the \
creaking, wooden ceiling. Brown stains drip from the wall's green wallpapper, some of which is torn, \
revealing the walls innards. The only things not desheveled and unkempt are a wooden table and \
chair in the center of the room. Odd... Given the state of the room, the two look almost brand new \
if it weren't for the the sunbleached sides nearest to the window. There are two doors: one that \
looks to be ajar to the east, and another shut to the south.", ["key", "book","6-pack"])
    r2 = Room("Room 2", "You walk into a cold room that seems to at one point served as a living \
room. An intricate fireplace made of carefully placed stones and bricks is the first to catch \
your eye. The feature is barren from any decoration, still with black soot staining the undersides \
of the overhanging bricks and spent ashes inside. An intact lighter lays at it's base on the floor. \
It was definitly well used. Maybe you could find something flamable to burn to heat the room. From \
admirring the fire place, you find yourself atop a rug that spans nearly the entire length of the \
room. All along the sides are tied knotes, fraid and desheveled. It's pattern resembles something \
that you would see on the back of some traditional playing card, but with far more detail. \
Something about it looks to be foreign-made. There are two doors: the one you just came from to \
the west, and another shut to the south.", ["torn_book","lighter","page","6-pack"])
    r3 = Room("Room 3", "This room reaks of rot. Half-standing bookshelves line the walls, but \
all of the books are either missing or have been torn apart and discarded at their feet. Stray \
pages that are notated in a language that isn't familiar to you litter the ground. A small desk \
occupies a corner of the room near the far wall. Atop the desk sits a statue of some sort \
that cradles the only intact book in the room. The torn cover features letters that you can read \
but lack enough to provide any valuable information. The other parts of the cover might be amidst \
the graveyard of skewed papers and spines, but it's no use searching for it. The only door is \
to the the north, the one you came from.", ["6-pack"])
    r4 = Room("Room 4", "You find yourself, in a near pitch black room, with the only light coming \
from the fireplace leaking past the door. The walls and whatever are along them are shaded beyond \
recognition. The only identifiable object in the room is some sort of modified brew rig directly \
opposite the door you came from. From the looks of it, the purpose of the additions seems to allow \
for the ability to add precise measurements of solutions to the brew. Alchemy maybe? A 6-pack of \
finished brew sits at it's base. There is suprisingly little that you can see within the once \
frightening room.", ["6-pack"])
    r5 = Room("Room 5", "You are in a bright place, an empty place. The ground is white and looks \
to go on forever in all directions. The sky is a faded blue, similar to the sky, but lacks the sun \
and any clouds. You squint into the distance to find any sort of identifiable features. Nothing. \
This place is barren. It's just you, your bag, and... someone else? You turn to see them more \
cleary. You recognize their face though you've never seen them before. Somehow you know them by \
the name 'Caleb'.",[])

#Moddifying Rooms
    r1.addExit("east",r2)
    r1.addExit("south",r3)
    r1.addGrab("key", "It is a golden key with intricate notched teeth in a pattern you've never seen before.")
    global key_IsUsed
    key_IsUsed = False
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")

    r2.addExit("west", r1)
    r2.addExit("south", r4)

    r2.addGrab("lighter", "It's of a unique design and definitely very old.")
    global lighter_isUsed
    lighter_isUsed = False

    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes. A lighter rests beside it.")
    r2.addItem("ashes", "Some spent ashes. Maybe if you find something flammable to burn, you could start the fire.")
    

    r3.addExit("north", r1)
    
    r3.addGrab("book", "The cover is too torn up to read. Many pages are missing.")
    global torn_book_IsUsed
    torn_book_IsUsed = False
    global page_IsUsed
    page_IsUsed = False


    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "It's of a weird figure holding a book.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    
    r4.addExit("north", r2)
    r4.addExit("south", r5)
    
    r4.addGrab("6-pack", "A strange smell is coming from it. Should you drink it?")
    global sixpack_IsUsed
    sixpack_IsUsed = False

    r4.addItem("brew_rig", "It looks to be heavily modified for alchemic purposes. A 6-pack is resting beside it.")

    r5.addNPC("caleb", ["'Ah ha! You've finaly made it! Congratulations! Welcome to my mind, it's a place of my own imagination! \
Quite impesive huh? Took me longer than expected to get everything how I wanted, but I think it turned out pretty alright, \
despite the messy state it's in at the moment. Anyways, come talk to me if you have any other questions and enjoy your stay!'","'\
Sorry for the mess... I could go about cleaning it all up and getting into every nook and crany, but do you know how long that \
would take? Ain't nobody got time for that, especially me! Having to keep up with everything out there can be quite a stresfull \
and time consuming task, so that's why I made this place! A place of my own where I'm in control! A place where I can come to and \
not worry about the wilting nature of time.'","'You could stay here forever if you want. You know, keep me company? If you don't \
want to, that's cool too. I'll just be here. All by myself. Alone. Sad...\n...\n...\nOh! You're still here.'","'If you want to \
leave, the door is just south of here'. A door appears to the south. 'It will lead you home, back to... um... Huh. Wait, I don't \
remember creating you. How did did you get here? If you were one of my creations, you would just be sent back to nothing, because \
that's where you came from. But you did'nt, so I don't know where you'll end up. Anyways, wherever you go, I hope you'll be happy \
there. It's been nice talking with you, Zakaria. A bit of a one-sided conversation, but a good one nonetheless. Farewell...'","'\
Oh, you're still here? Well I guess we could talk a bit more if you'd like. Oooh, Ive got a joke for you! What do you call a fish \
wearing a bowtie?\n...\nSofishticated!\n...\nSorry...'","'You know, I can't stop thinking about what you are. You didn't come from \
my imagination, and you couldn't have come from anywhere else. My theory? You are a real person controlling a theoretical character \
inside my own mind through some kind of advanced technology. I bet that's it.'","'Ever heard of a great eared nightjar? It's a \
species of bird native to south-east Asia and they're like little dragons. Their feathers are so poofy it makes them look like \
they have little ears. They're so cute!'","'bgthNEaTgBagebtbvatbBBTBTBcAEabtTTobBbtbBBB! How do you like my sea lion impression?'",
"'Did you know that you cant look up and stick you're tongue out at the same time? Don't believe me? Try it. \n...\nBAHAH, you \
actually fell for it! You look so stupid right now. ahahha!'","'I need to stop writing dialogue for this npc that is supposed to \
be a digital representation of myself in a world that I created from what was supposed to be a simple coding activety, and finish \
writing the actual functioning code... I think I broke the fourth wall a bit too much...'","'Why are you still here?'",])
    global Caleb_talkcounter
    Caleb_talkcounter = 0

    currentRoom = r1

    #End Create Rooms

def roomDescUpdate():
    print("="*56)
    #Room name
    if currentRoom == None:
        print("...")
    else:
        s = f"You find yourself in {currentRoom.name} "

        if customRoomDesc == True:
            print(currentRoom.rdesc)

        else:
            #Doors
            if len(currentRoom.exits) == 0:
                s += "with no doors. "
            elif len(currentRoom.exits) == 1:
                s += f"with a single door leading {currentRoom.exits[0]}. "
            elif len(currentRoom.exits) == 2:
                s += f"with doors leading to the {currentRoom.exits[0]} and to the {currentRoom.exits[1]}. "
            else:
                s += "with doors leading "
                for i in range(len(currentRoom.exits)-1):
                    s += f"to the {currentRoom.exits[i]}, "
                s += f"and to the {currentRoom.exits[-1]}. "

            #Items
            s += "As you look around, you can spot "
            if len(currentRoom.items) == 0:
                s += "nothing."
            elif len(currentRoom.items) == 1:
                s += f"a {currentRoom.items[0]}. "
            elif len(currentRoom.items) ==2:
                s += f"a {currentRoom.items[0]} and a {currentRoom.items[1]}. "
            else:
                for i in range(len(currentRoom.items)-1):
                    s += f"a {currentRoom.items[i]}, "
                s += f"and a {currentRoom.items[-1]}. "

            

            print(s)

    print("="*56)

def getOption1():
    global customRoomDesc
    customRoomDesc = False
    userin = input("Would you like to play with the default generated room descriptions or more \
descriptive and immersive descriptions?\n<NOTE> Custom descriptions highly recomended. Auto \
generated descriptions are not supported after room 3 and lots of details are omitted.\nY/n ")
    if userin.lower() in("n","no","na","nah"):
        print("Playing with auto generated room descriptions. Enjoy!")
    else:
        customRoomDesc = True
        print("Now playing with custom descriptions. Enjoy!")



#GAME START
getOption1()
input("Press ENTER to start game")
print("\n"*10)
inventory = []
inventoryidesc = []
createRooms()
roomDescUpdate()


while True :
    if currentRoom == None:
        break
#dictionaries
    actionhelp = {
        "help", "idk", "assist", "assistance", "?"
    }
    action0 = {
        "quit", "exit", "bye", "end"
    }
    action1 = {
        "go", "walk", "run", "continue"
    }
    action2 = {
        "look", "inspect", "obsverve"
    }
    action3 = {
        "take", "grab", "get", "steal", "pickup", "pick_up", "nab", "yoink", "stash", "stow"
    }
    action4 = {
        "use"
    }
    action5 = {
        "talk", "speak", "converse", "chat" 
    }
    action6 = {
        "inventory", "bag", "backpack", "pack", "items"
    }

#actions
    userin = input("What do you do? \n")
    userin = userin.lower()
    
    if userin in(action0):
        print("Exiting Game...")
        break

    elif userin in(actionhelp):
        response = "<<< HELP PAGE >>>\n\
help - Shows a list of available commands (You are here now). \n\tUSAGE : help \n\
go - Used to navigate around to other rooms. \n\tUSAGE : go <cardinal direction> \n\
look - Used to gain more information on items. Can be used inside inventory. \n\tUSAGE : look <item> \n\
take - Used to take items with you for later use. \n\tUSAGE : take <item> \n\
use - Used to use items in your inventory in certain locaitions. \n\tUSAGE : use <item> \n\
bag - Used to view item in your inventory. \n\tUSAGE : bag \n\
back - Used to exit your inventory. \n\tUSAGE : back \n\
quit - Used to quit the game. \n\tUSAGE : quit \n\n\
NOTE : Most commands have alliases that do the same thing, such as go and walk, or take and grab, icluding many more!"

#inventory actions
    elif userin in(action6):
        print("\n"*10)
        print("You open your bag to see your items.\n")
        while True:
            response = "="*56
            response += "\nInside your bag, you find "
            if len(inventory) == 0:
                response += "nothing. Good ol' nothing. "
            elif len(inventory) == 1:
                response += f"a {inventory[0]}. "
            elif len(inventory) ==2:
                response += f"a {inventory[0]} and a {inventory[1]}. "
            else:
                for i in range(len(inventory)-1):
                    response += f"a {inventory[i]}, "
                response += f"and a {inventory[-1]}. "
            response += "\n"
            
            response += "="*56
            print(response)
            userin = input("You may inspect your items or type `back` to go resume. \n").lower()
            userin = userin.lower()
            if userin == "back":
                response = "You close your bag and continue on your way."
                break
            else:
                userin = userin.split()
                response = "I don't understand. Use `help` for more information.\n"
                if len(userin)==2:
                    useract = userin[0]
                    userobj = userin[1]
                # look action #
                    if useract in(action2):
                        response = f"You do not have a {userobj} in your bag."
                        # items #
                        if userobj in(inventory):
                            x = random.randint(0,2)
                            if x == 0:
                                response = f"You reach for your {userobj} "
                            if x == 1:
                                response = f"You pull out your {userobj} "
                            if x == 2:
                                response = f"You take out your {userobj} "
                            x = random.randint(0,2)
                            if x == 0:
                                response += "for inspection. "
                            if x == 1:
                                response += "to study it. "
                            if x == 2:
                                response += "to look at it closely. "

                            response += inventoryidesc[inventory.index(userobj)] + "\n"
                print("\n"*10)
                print(response)

    #combo actions
    else:
        userin = userin.split()
        response = "I don't understand. Use `help` for more information."

        if len(userin)==2:
            useract = userin[0]
            userobj = userin[1]

            # go action
            if useract in(action1):
                response = "There is no door here."
                if currentRoom.name == "Room 1" and userobj == "south" and key_IsUsed == False:
                    response = "The door is locked."
                elif currentRoom.name == "Room 2" and userobj == "south" and page_IsUsed == False:
                    response = "The door is locked with a combination lock."
                elif currentRoom.name == "Room 4" and userobj == "south":
                    response = "There is no door here."
                elif userobj in(currentRoom.exits):
                    response = f"You {useract} through the {userobj} door. "
                    currentRoom = currentRoom.exitL[currentRoom.exits.index(userobj)]
            # look action
            elif useract in(action2):
                response = f"You cannot find a {userobj}."
                if userobj in(currentRoom.items) or userobj in(currentRoom.grabs):
                    x = random.randint(0,2)
                    if x == 0:
                        response = "Out of the corner of your eye, y"
                    if x == 1:
                        response = "After a quick glance, y"
                    else:
                        response = "Y"

                    x = random.randint(0,5)
                    if x == 0:
                        response += "ou find a "
                    elif x == 1:
                        response += "ou spot a "
                    elif x == 2:
                        response += "ou happen to find a "
                    elif x == 3:
                        response += "ou happen to spot a "
                    elif x == 4:
                        response += "ou manage to find a "
                    else:
                        response += "ou manage to spot a "
                    if userobj in(currentRoom.items):
                        response += f"{userobj}. {currentRoom.idesc[currentRoom.items.index(userobj)]}"
                    else:
                        response += f"{userobj}. {currentRoom.gdesc[currentRoom.grabs.index(userobj)]}"
    
        # grab action
            elif useract in(action3):
                response = f"You cannot find a {userobj}."
                if userobj in(currentRoom.grabs):
                    response = f"You {useract} the {userobj}."
                    inventory.append(userobj)
                    inventoryidesc.append(currentRoom.gdesc[currentRoom.grabs.index(userobj)])
                    currentRoom.delGrab(userobj)
                    # item and room description changes
                    if userobj == "key":
                        currentRoom.idesc[currentRoom.items.index("table")] = "It is made of oak \
and lacking the key you took from it."
                    if userobj == "book":
                        currentRoom.rdesc = "This room reaks of rot. Half-standing bookshelves \
line the walls, but all of the books are either missing or have been torn apart and discarded at \
their feet. Stray pages that are notated in a language that isn't familiar to you litter the \
ground. A small desk occupies a corner of the room near the far wall. Atop the desk sits a statue \
of some sort that used to hold the book you took from it. In a weird way, the statue almost looks \
sad, as if a part of it's soul is missing. You almost feel bad. You monster. The only door is \
to the the north, the one you came from."
                        currentRoom.idesc[currentRoom.items.index("statue")] = "It's of a weird \
figure positioned to be holding the book you took from it. It almost looks sad without it's book."
                        currentRoom.idesc[currentRoom.items.index("desk")] = "It is made of \
stained birch. A statue positioned to hold the book you took from it is resting on the desk."
                    if userobj == "lighter":
                        currentRoom.rdesc = "You walk into a cold room that seems to at one point served \
as a living room. An intricate fireplace made of carefully placed stones and bricks is the first to catch \
your eye. The feature is barren from any decoration, still with black soot staining the undersides \
of the overhanging bricks and spent ashes inside. It was definitly well used. Maybe you could find \
something flamable to burn to heat the room. From admirring the fire place, you find yourself atop \
a rug that spans nearly the entire length of the room. All along the sides are tied knotes, fraid \
and desheveled. It's pattern resembles something that you would see on the back of some traditional \
playing card, but with far more detail. Something about it looks to be foreign-made. There are two \
doors: the one you just came from to the west, and another shut to the south."
                        currentRoom.idesc[currentRoom.items.index("fireplace")] = "It is full of ashes."
                        if torn_book_IsUsed == True:
                            currentRoom.idesc[currentRoom.items.index("fireplace")] = "Inside, your torn \
book rests on a pile of ashes."
                    if userobj == "6-pack":
                        currentRoom.idesc[currentRoom.items.index("brew_rig")] = "It looks to be heavily \
modified for alchemic purposes."
                    
                if userobj in(currentRoom.items):
                    response = f"You cannot {useract} the {userobj}. "
                    y = random.randint(0,3)
                    if y == 1:
                        response += "Stop."
                    if y == 2:
                        response += f"You'd {useract} something smaller, but a {userobj}? Seriously?"
                    if y == 3:
                        response += f"What kind of person would {useract} another man's {userobj}?"

        # use action
            elif useract in(action4):
                response = f"You do not have a {userobj} to {useract}"
                if userobj in(inventory):
                    response = f"You cannot {useract} the {userobj} here. "

                    if userobj == "key" and userobj in(currentRoom.ruse) and key_IsUsed == False:
                        response = f"You {useract} the {userobj}. The southern door unlocks."
                        if customRoomDesc == True:
                            response = "You noticed the south door was locked. Maybe the key can \
unlock it. The key slides into the mechanism almost perfectly. As you twist, a small click sounds \
from within. You turn the door handle and the door creaks open."
                        key_IsUsed = True
                        currentRoom.rdesc = "You find yourself in a bright room with what seems to be \
once-was furnature scattered about the corners of the room and covered with a blanket of dust. The \
setting sun's light illuminates the wall through an opposing window, catching specs of floating dust \
falling from the creaking, wooden ceiling. Brown stains drip from the wall's green wallpapper, some of \
which is torn, revealing the walls innards. The only things not desheveled and unkempt are a wooden \
table and chair in the center of the room. Odd... Given the state of the room, the two look almost \
brand new if it weren't for the the sunbleached sides nearest to the window. There are two doors: one \
that looks to be ajar to the east, and the other unlocked door to the south."

                    elif userobj == "book" and userobj in(currentRoom.ruse):
                        response = "In the sunlight, you find an intact page that looks important. \
You tear the page from the spine and stow it for later."
                        if customRoomDesc == True:
                            response = "Using the sunlight beaming from the window, you flip through \
the strange book in hopes of finding anything useful. The pages seem to depict illustrations and \
schematics paired with frequent equations and notation, but again, everything is in a language you \
don't understand. Near the last few pages, you find a page that reads 'A story, forbiden be told.' \
followed by a list of random numbers mixed with unfamiliar symbols. As it's the only page useful \
to you right now, you tear if from the book and stow it in your bag for later. You also return your \
now-torn book to your bag."
                        inventoryidesc.remove(inventoryidesc[inventory.index(userobj)])
                        inventory.remove(userobj)
                        inventory.append("torn_book")
                        inventoryidesc.append("The cover is too torn up to read. What's left of the pages \
are written in an unfamiliar language. It's only use to you now is it's material value. Maybe it could serve \
as good make-shift firewood. Who knows...")
                        inventory.append("page")
                        inventoryidesc.append("A page torn from the book you found on the statue. \
It reads 'A story, forbiden be told.' followed by a list of random numbers mixed with unfamiliar symbols.")

                    elif userobj == "torn_book" and userobj in(currentRoom.ruse):
                        response = "You discard your book into the fire place to be burned. All you need \
now is a way to light it."
                        if customRoomDesc == True:
                            response = "Your torn book holds no value to you other than it's material \
value. You retreve it from your bag and discard it atop the spent ashes in the fire place, ready to \
serve it's final purpose."
                        inventoryidesc.remove(inventoryidesc[inventory.index(userobj)])
                        inventory.remove(userobj)
                        currentRoom.rdesc = "You walk into a cold room that seems to at one point served \
as a living room. An intricate fireplace made of carefully placed stones and bricks is the first to catch \
your eye. The feature is barren from any decoration, still with black soot staining the undersides \
of the overhanging bricks and your discarded torn book sitting spent ashes inside, waiting to be lit. \
From admirring the fire place, you find yourself atop a rug that spans nearly the entire length of the \
room. All along the sides are tied knotes, fraid and desheveled. It's pattern resembles something that \
you would see on the back of some traditional playing card, but with far more detail. Something about it \
looks to be foreign-made. There are two doors: the one you just came from to the west, and another shut \
to the south."
                        currentRoom.idesc[currentRoom.items.index("fireplace")] = "Inside, your torn book \
rests on a pile of ashes. A lighter rests beside it."
                        if "lighter" in inventory:
                            currentRoom.idesc[currentRoom.items.index("fireplace")] = "Inside, your torn book \
rests on a pile of ashes."
                        currentRoom.idesc[currentRoom.items.index("ashes")] = "Some spent ashes with your \
flammable and torn book resting atop them."
                        torn_book_IsUsed = True
                        
                    elif userobj == "lighter" and userobj in(currentRoom.ruse):
                        response = "There is nothing to light in the fireplace."
                        if torn_book_IsUsed == True:
                            response = "You set your torn bood aflame in the fire place with your lighter. \
Warmth fills the room as it lights."
                            if customRoomDesc == True:
                                response = "You set your torn bood aflame in the fire place with your lighter. \
Warmth fills the room as it lights. As the flame touches the book's leathery cover, it bursts into a frenzy of \
dancing deep red flames. It sizzles in the heat, it's spine falling appart as what's left of the pages burn into \
flying embers. You almost feel bad as it's wailing sizzles sound throughout the room. At least you're warm..."
                            inventoryidesc.remove(inventoryidesc[inventory.index(userobj)])
                            inventory.remove(userobj)
                            inventoryidesc[inventory.index("page")] = "A page torn from the book you found on the \
statue. It reads 'A story, forbiden be told.' followed by a list of random numbers mixed with unfamiliar symbols. \
But, somthing is different... A small portion of the numbers are underlined with red ink. Or is that blood..."
                            currentRoom.rdesc = "You walk into a warm room that seems to at one point served as a \
living room. An intricate fireplace made of carefully placed stones and bricks is the first to catch your eye. The \
feature is barren from any decoration, still with black soot staining the undersides of the overhanging bricks and \
your burning torn book inside, casting light and warmth into the room. From admirring the fire place, you find \
yourself atop a rug that spans nearly the entire length of the room. All along the sides are tied knotes, fraid \
and desheveled. It's pattern resembles something that you would see on the back of some traditional playing card, \
but with far more detail. Something about it looks to be foreign-made. There are two doors: the one you just came \
from to the west, and another shut to the south."
                            currentRoom.idesc[currentRoom.items.index("fireplace")] = "A fire is lit inside of it."
                            currentRoom.idesc[currentRoom.items.index("ashes")] = "The ashes do little to support \
the burning book resting on them."
                            lighter_isUsed = True

                    elif userobj == "page" and lighter_isUsed == True and userobj in(currentRoom.ruse):
                        response = "Maybe the random list of numbers on the page has something to do with the \
the password for the door's combination lock, but nothing seems to stand out right now. Start the fireplace, \
take a seat, get comfy, because decyphering the page might take a while."
                        if "torn_book" not in(inventory):
                            response = "You find a portion of underlined numbers on your page and input it \
into the south door's combination lock. It opens and your page flies into the dark room. You're having second \
thought about entering now."
                            if customRoomDesc == True:
                                response = "You look at the page you tore from the now burning book. Some of \
the numbers are underlined in red ink. You can't remember if that was there before. Weird... You wonder what \
what it means. Maybe it's a date? It could be a, an ID number of some sort? Wait. You needed a password to \
open the south door. That's probably it! You input the numbers into the lock and it clicks. The door \
cracks open to reveal a dark room. You go to push the door open, the page flies from your hand and slips \
past the door into the room, disappearing into the darkness. You cautiously back away. Maybe you shouldn't \
go in there... "
                            page_IsUsed = True
                            inventoryidesc.remove(inventoryidesc[inventory.index(userobj)])
                            inventory.remove(userobj)
                        currentRoom.rdesc = "You walk into a warm room that seems to at one point served as a \
living room. An intricate fireplace made of carefully placed stones and bricks is the first to catch your eye. The \
feature is barren from any decoration, still with black soot staining the undersides of the overhanging bricks and \
your burning torn book inside, casting light and warmth into the room. From admirring the fire place, you find \
yourself atop a rug that spans nearly the entire length of the room. All along the sides are tied knotes, fraid \
and desheveled. It's pattern resembles something that you would see on the back of some traditional playing card, \
but with far more detail. Something about it looks to be foreign-made. There are two doors: the one you just came \
from to the west, and another cracked door to the south, leading to an eerie darkness beyond."

                    elif userobj == "6-pack" and sixpack_IsUsed == False:
                        response = f"You drink the {userobj}. As you finish drinking, you discard the bottle \
into your bag. Your vision goes blury and the room tilts. You fall to the ground as your conscience fades. You \
wake after some time. "
                        if customRoomDesc == True:
                            response = "You pop the lid from the bottle. It smells like rotting strawberries \
mixed with a strong chemical smell. Oh well, down the hatch! You tilt back and take a big swig. the taste is \
suprisingly not bad. Wiping the excess from your lips, you discard the bottle back into your bag. Aside from \
the odd after-taste, the brew wasnt all that bad. Wait, is the room getting darker? Your vision goes blury \
and the room begins to tilt. You fall to the ground as your conscience fades. After an unknown amount of time, \
you wake."
                        sixpack_IsUsed = True
                        inventory.remove(userobj)
                        inventory.append("bottle")
                        inventoryidesc.append("Its empty after drinking the brew it previously contained.")
                        currentRoom = currentRoom.exitL[currentRoom.exits.index("south")]

                    else:
                        if userobj == "key":
                            response += f"You can't find any thing that the {userobj} will go to."
                        elif userobj == "book":
                            response += f"It's too dark to read the {userobj}."
                        elif userobj == "torn_book":
                            response = f"And how exactly are you going to {useract} your {userobj} here? \
Throw it at things and hope something happens? You cannot {useract} your {userobj} here."
                        elif userobj == "page" and currentRoom.name == "Room 2":
                            response += "Maybe the random list of numbers on the page has something to do \
with the the password for the door's combination lock, but nothing seems to stand out right now. Start the \
fireplace, take a seat, get comfy, because decyphering the page might take a while."
                        elif userobj == "lighter":
                            response += "Lighting the room on fire with you in it is probably not a good \
idea."

        # talk action
            elif useract in action5:
                response = f"{userobj} is not here."
                if userobj in currentRoom.npc:
                    if userobj == "caleb":
                        if Caleb_talkcounter < 4:
                            response = currentRoom.npcdialogue[currentRoom.npc.index(userobj)][Caleb_talkcounter]
                            Caleb_talkcounter += 1
                            if Caleb_talkcounter == 4:
                                currentRoom.addExit("south", None)
                        else:
                            response = currentRoom.npcdialogue[currentRoom.npc.index(userobj)][random.randint(4,10)]

    print("\n"*10)
    print(f"{response}\n")
    roomDescUpdate()



#                _________________________________________________
#               |                                                 |
#               | It seems that there is nothing here. It's dark. |
#               | The sky is filled with wonderfull colors, and   |
#               | it's beautiful. I see no way out. The only      |
#               | option I can see is a red 'x' in the distance.  |
#               | I'm not certain what will happen once I reach   |
#               | it, but I fear this is the only way out.        |
#               | Goodbye, my friend...                           |
# |\/\/\/|      | ________________________________________________|
# |      |      |/
# | (o)(o)  
# C      _) 
#  |  ___|  
#  |   /    
# /____\    
#/      \