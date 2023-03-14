class Character:
    def __init__(self, name, descr):
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.description = descr
        self.convers = ''

    def name_descr(self):
        print(f'There is {self.name}')
        print(f'{self.description}')

    def set_conversation(self, convers):
        '''
        Sets conversation with enemy
        '''
        self.convers = convers

    def talk(self):
        '''
        Makes a user talk with the enemy
        '''
        print('\n')
        print(f'[{self.name} says]: {self.convers}')


class Cavaler(Character):
    def __init__(self, name, descr):
        super().__init__(name, descr)

    def yes(self,command,backpack):
        if command.lower() == 'yes':
            print('Now you have weapon')
            backpack.append('weapon')

class Homeless(Character):
    def __init__(self, name, descr):
        super().__init__(name, descr)

    def help(self, command, backpack):
        if command.lower() == 'help':
            print('Now you have a hint')
            print('Your hint word is "Weather"')
            backpack.append('hint')
            return 'Weather'


class Robber(Character):
    def __init__(self, name, descr):
        super().__init__(name, descr)

class Boss(Character):
    def __init__(self, name, descr):
        super().__init__(name, descr)

    def set_weakness(self, weak):
        self.weak = weak


class Street():
    def __init__(self, name):
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.descr = None
        self.chrct = None

    def set_description(self, descr):
        self.descr = descr

    def get_details(self, next):
        print(self.name)
        print('- - - - - - - - - - - - - -')
        print(f'{self.descr}')
        print(f'Next street is {self.name}')

    def set_character(self, chrct):
        '''
        Sets character of the room
        '''
        self.chrct = chrct

    def get_character(self):
        return self.chrct
