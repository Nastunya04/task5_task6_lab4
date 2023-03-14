'''
3 classes:
• class Room - has methods and attributes, which describe room
• class Enemy - has methods and attributes, which describe enemy
• class Item - has methods and attributes, which describe item
'''
class Room:
    '''
    Has methods and attributes, which describe room
    '''
    def __init__(self, name):
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.sntnc = None
        self.rooms_direct = {}
        self.character = None
        self.items = None

    def set_description(self, sntnc):
        '''
        Sets description of the room
        '''
        self.sntnc = sntnc

    def link_room(self, room, direct):
        '''
        Links room
        '''
        self.rooms_direct[direct] = room
        # print(self.rooms_direct)

    def set_character(self, character):
        '''
        Sets character of the room
        '''
        self.character = character

    def get_details(self):
        '''
        Gets details of the room
        '''
        print(self.name)
        print('--------------------')
        print(self.sntnc)
        for key, value in self.rooms_direct.items():
            print(f'The {value.name} is {key}')

    def get_character(self):
        '''
        Gets character of the room
        '''
        return self.character

    def set_item(self, items):
        '''
        Sets item of the room
        '''
        self.items = items

    def get_item(self):
        '''
        Gets item of the room
        '''
        return self.items

    def move(self, command):
        '''
        Moves to another room
        '''
        return self.rooms_direct[command]

class Enemy():
    '''
    Has methods and attributes, which describe enemy
    '''
    enem = []
    def __init__(self, name, description) -> None:
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.description = description
        self.convers = ''
        self.weak = None

    def set_conversation(self, convers):
        '''
        Sets conversation with enemy
        '''
        self.convers = convers

    def set_weakness(self, weak):
        '''
        Sets weakness of the enemy
        '''
        self.weak = weak

    def describe(self):
        '''
        Describes the enemy
        '''
        print(f'{self.name} is here!')
        print(f'{self.description}')

    def talk(self):
        '''
        Makes a user talk with the enemy
        '''
        print(f'[{self.name} says]: {self.convers}')

    def fight(self, fight_with):
        '''
        Makes a user talk with the enemy
        '''
        if fight_with == self.weak:
            print(f'You fend {self.name} off with the {self.weak}')
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False

    def get_defeated(self):
        '''
        Returns how many times where all enemies defeated
        '''
        Enemy.enem.append('loose')
        return len(Enemy.enem)

class Item:
    '''
    Has methods and attributes, which describe item
    '''
    def __init__(self, item) -> None:
        '''
        Lets the class initialize the object's attributes
        '''
        self.item = item
        self.descr = None

    def describe(self):
        '''
        Describes the item
        '''
        print(f'The [{self.item}] is here - {self.descr}')

    def set_description(self, descr):
        '''
        Sets a description of an item
        '''
        self.descr = descr

    def get_name(self):
        '''
        Gets name of the item
        '''
        return self.item
