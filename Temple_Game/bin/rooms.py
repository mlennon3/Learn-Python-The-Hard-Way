from sys import exit

def death():
    print "You died. Game over."
    exit(0)

class Hero(object):
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

    def is_alive(self, hp):
        if hp <= 0:
            print "%s is dead" % self.name
            death()
        else: 
            pass

    def battle(self, baddie):
        self.hp = self.hp - baddie.str
        print "%s's hp is now: %d" % (self.name, self.hp)
        hp = self.hp
        self.is_alive(hp)
        baddie.battle(self)

class Baddie(object):
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

    
    def is_alive(self, hp):
        if hp <= 0:
            print "%s is dead" % self.name
        else: 
            pass

    def battle(self, hero):
        self.hp = self.hp - hero.str
        print "%s's hp is now: %d" % (self.name, self.hp)
        hp = self.hp
        self.is_alive(hp)



michael = Hero("Michael", 10, 10)

def start():
    return entrance()

class entrance(object):
    def __init__(self):
        pass
    def play(self):
        print "You are standing at the entrance to a large temple"
        print "Would you like to face a challenge?"
        response = raw_input("y/n \n> ")
        if response == "y":
            return 'three_door_room'
        else:
            exit(0)


class three_door_room(object):
    def __init__(self):
        pass
    def play(self):
        print "You enter a low-ceilinged room with no windows.  There are three wide doors,"
        print "one to the left, the second straight ahead, and the third to your right."
        print "Which will you choose to enter?"
        response = raw_input("> ")
        if response == "1":
            return 'red_room'
        elif response == "2":
            return 'green_room'
        elif response == "3":
            return 'blue_room'
        else:
            print "Come again?"
            return 'three_door_room'

class red_room(object):
    def __init__(self):
        pass
    def play(self):
        print "This room is red..."
        print "Ahh a bear!!"
        michael.battle(bear)
        print "Quick, open that door over there"
        return 'blue_room'
        

class green_room(object):
    def __init__(self):
        pass
    def play(self):
        print "This is a small green closet with a door on the other side"
        print "Ahh attacked by a bat!"
        michael.battle(bat)
        print "Press any key to enter the door"
        response = raw_input("> ")
        if response:
            print "You're headed back outside."
            return 'entrance'

class blue_room(object):
    def __init__(self):
        pass
    def play(self):
        print "This room is blue..."
        response = raw_input("What next? \n > ")
        print "Shit a spider!"
        michael.battle(spider)
        return 'entrance'


spider = Baddie("Spider", 1, 1)
bat = Baddie("Bat", 2, 2)
wolf = Baddie("Wolf", 4, 3)
bear = Baddie("Bear", 6, 6)
        

            
        


