'''
• class Character
• class Cavaler(Character)
• class Homeless(Character)
• class Robber(Character)
• class Boss(Character)
• class Street
'''
class Character:
    '''
    class Character
    '''
    def __init__(self, name, descr):
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.description = descr
        self.convers = ''

    def name_descr(self):
        '''
        Name description
        '''
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
        '''
        Lets the class initialize the object's attributes
        '''
        super().__init__(name, descr)

    def yes(self,command,backpack):
        '''
        If input is yes, does smth
        '''
        if command.lower() == 'yes':
            print('Now you have weapon')
            backpack.append('weapon')

class Homeless(Character):
    '''
    class Homeless, inherited from Character
    '''
    def __init__(self, name, descr):
        '''
        Lets the class initialize the object's attributes
        '''
        super().__init__(name, descr)

    def help(self, command, backpack):
        '''
        If input is help, does smth
        '''
        if command.lower() == 'help':
            print('Now you have a hint')
            print('Your hint word is "Weather"')
            backpack.append('hint')
            return 'Weather'


class Robber(Character):
    '''
    class Robber, inerited from Character
    '''
    def __init__(self, name, descr):
        '''
        Lets the class initialize the object's attributes
        '''
        super().__init__(name, descr)

class Boss(Character):
    '''
    class Boss, inherited from Character
    '''
    def __init__(self, name, descr):
        '''
        Lets the class initialize the object's attributes
        '''
        super().__init__(name, descr)


class Street():
    '''
    class Street
    '''
    def __init__(self, name):
        '''
        Lets the class initialize the object's attributes
        '''
        self.name = name
        self.descr = None
        self.chrct = None

    def set_description(self, descr):
        '''
        Sets description for Street
        '''
        self.descr = descr

    def get_details(self):
        '''
        Prints details of street
        '''
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
        '''
        Gets character
        '''
        return self.chrct
