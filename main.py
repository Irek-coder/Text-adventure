from room import Room
from character import Character, Enemy, Friend
from item import Item
print("""Controls are:
"North/East/South/West" are for movement
"fight" is for fighting
"hug" is for hugging
"pick up" is for picking up items
"check bag" is for checking your backpack
"talk" is for talking
"bribe" is for bribing""")
available=False
backpack=[]
alive=True
kitchen=Room("Kitchen")
##print(kitchen.description)
kitchen.description="A place where you don't know 48 different objects in English"
##print(kitchen.description)
bunker=Room("Bunker")
bunker.set_description("A bunker")
nuclearbomb=Item("a literal nuclear warhead")
nuclearbomb.set_description("Like a weapon which actually breaks the Geneva Conventions")
bunker.set_item(nuclearbomb)
bunker.link_room(kitchen,"South")
kitchen.link_room(bunker,"North")

dining_hall=Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
dining_hall.link_room(kitchen,"North")
kitchen.link_room(dining_hall,"South")

ballroom=Room("Ballroom")
ballroom.set_description("A place where people dance at parties")
ballroom.link_room(dining_hall,"East")
dining_hall.link_room(ballroom,"West")

jon=Friend("Jon","An old pal. ")
jon.set_conversation("Sah dude")
##dining_hall.get_details()
##print()
##kitchen.get_details()

current_room=kitchen
dave=Enemy("Dave","A smelly zombie.")
##dave.describe()
##dave.talk()
dave.set_conversation("bruh bruh bruh bruh bruh")
##dave.talk()
##
dave.set_worth(5)
dave.set_weakness("cheese")
##print("What will you fight with?")
##fight_with=input()
##dave.fight(fight_with)
dining_hall.set_character(dave)
ballroom.set_character(jon)
cheese=Item("cheese")
cheese.set_description("Dave really likes these")
kitchen.set_item(cheese)
while alive==True:

    print("\n")
    current_room.get_details()
    item=current_room.get_item()
    inhabitant=current_room.get_character()
    if item != None:
        print(item.name)
        item.describe()
        itemless=False
    else:
        itemless=True
    if inhabitant is not None:
        inhabitant.describe()
        empty=False
    else:
        empty=True
    command=input("> ")
    if command in ["North","East","South","West"]:
        current_room=current_room.move(command)
    elif command=="check bag":
        if backpack==[]:
            print("backpack is empty!")
        else:
            for items in backpack:
                print(items.name)
    elif command=="pick up" and itemless==False:
        print("Picked up "+current_room.item.name)
        backpack.append(current_room.item)
        current_room.set_item(None)
    elif command=="pick up" and itemless==True:
        print("no items found in room")
    elif command=="fight" and empty==False and backpack!=[]:
        print("What do you want to fight "+inhabitant.name+" with? ")
        print("Available items:")
        for items in backpack:
            print(items.name)
        weapon=input()
        for name in backpack:
            if weapon==name.name:
                available=True
            else:
                pass
        if available==False:
            print("You don't have that weapon!")
        else:
            if inhabitant.fight(weapon) and available==True:
                alive=True
                available=False
            else:
                alive=False
                available=False
        
    elif command=="talk" and empty==False:
        inhabitant.talk()
    elif command=="bribe" and empty==False and isinstance(inhabitant,Enemy):
        amount=int(input("How much do you want to bribe "+inhabitant.name+" with?"))
        if inhabitant.bribe(amount):
            pass
        else:
            weapon=input("What do you want to fight "+inhabitant.name+" with? ")
            inhabitant.fight(weapon)
    elif command=="hug" and empty==False and isinstance(inhabitant,Friend):
        inhabitant.hug()
    elif command=="talk" or "fight" or "bribe" and empty==True:
        print("Room is empty! ")

input()
