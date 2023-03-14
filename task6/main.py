import game1

doroshenka_st = game1.Street('Doroshenka St.')
doroshenka_st.set_description("Welcome to the one of Lviv's most beautiful streets")

bandery_st = game1.Street('Bandery St.')
bandery_st.set_description("Welcome to the street where the most \
famous Lviv Polytechnic building is located")

antonovycha_st = game1.Street('Antonovycha St.')
antonovycha_st.set_description("Welcome to the street which was named \
in honor of one of the most famous Ukrainian historian and ethnographer Volodymyr Antonovych")

kulparkivska_st = game1.Street('Kulparkivska St.')
kulparkivska_st.set_description("Welcome to the street where the \
biggest shopping mall in Western Ukraine is located")

horodotska_st = game1.Street('Horodotska St.')
horodotska_st.set_description("Welcome to the longest street in Lviv")

nalyvaika_st = game1.Street('Nalyvaika St.')
nalyvaika_st.set_description("Welcome to the street which was named in honor \
of Severyn Nalyvaiko, a leader of the Ukrainian Cossacks")

hnatyuka_st = game1.Street('Akademika Hnatyuka St.')
hnatyuka_st.set_description("Welcome to the street which is named in honor of one of \
the most influential and notable Ukrainian ethnographers.")

cavaler_1 = game1.Cavaler('Marko', 'A man, who helps you to find a shop with weapon')
cavaler_1.set_conversation("It is really dangerous here! Do you want to go to a shop to buy some weapon?(enter 'yes' or 'no')")

cavaler_2 = game1.Cavaler('Ivan', 'A man, who helps you to find a shop with weapon')
cavaler_2.set_conversation("It is really dangerous here! Do you want to go to a shop to buy some weapon?(enter 'yes' or 'no')")

homeless_1 = game1.Homeless('Max', 'Very poor and unhappy man, but has a kind heart')
homeless_1.set_conversation('Give me anything you have and I will say you a hint, so in case you meet a boss,\
you will be able to say it to him')

boss_1 = game1.Boss('Oleksiy', 'Very dangerous and unfriendly man')
boss_1.set_conversation("You won't go anywhere! You can either kill me or say me \
a hint and I will let you go")

boss_2 = game1.Boss('Petro', 'Very dangerous and unfriendly man')
boss_2.set_conversation("You won't go anywhere! You can either kill me or say me \
a hint and I will let you go")

boss_3 = game1.Boss('Nazar', 'Very dangerous and unfriendly man')
boss_3.set_conversation("You won't go anywhere! You can either kill me or say me \
a hint and I will let you go")

marshrutka_robber_1 = game1.Robber('Sasha', 'Very unfair and impolite man, \
who robs people in marshrutkas')
marshrutka_robber_1.set_conversation("Ha-ha-ha, I am so fast, no one can catch me with my money")

doroshenka_st.set_character(cavaler_1)
bandery_st.set_character(boss_1)
antonovycha_st.set_character(marshrutka_robber_1)
kulparkivska_st.set_character(homeless_1)
horodotska_st.set_character(cavaler_2)
nalyvaika_st.set_character(boss_2)
hnatyuka_st.set_character(boss_3)

win = 0
num = 0

lst_of_streets = [doroshenka_st, bandery_st, antonovycha_st, kulparkivska_st, horodotska_st, nalyvaika_st, hnatyuka_st]
current_street = doroshenka_st
bag = []

dead_status = False


while dead_status is False:
    print("\n")
    current_street.get_details(lst_of_streets[num])
    if len(bag) == 0:
        print('You have nothing in your backpack')
    else:
        print(f"You have {', ' .join(map(str, bag))} in your backpack")
    inhabitant = current_street.get_character()

    if inhabitant is not None:
        inhabitant.name_descr()
        if inhabitant == cavaler_1:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    cavaler_1.talk()
                    command_2 = ''
                    while command_2 not in ('yes', 'no'):
                        command_2 = input('> ')
                        if command_2.lower() == 'yes':
                            cavaler_1.yes(command_2, bag)
                            current_street = lst_of_streets[1]
                            num += 1
                        elif command_2.lower() == 'no':
                            current_street = lst_of_streets[1]
                            num += 1
                        elif command_2 not in ('yes', 'no'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[1]
                    num += 1
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")

        elif inhabitant == boss_1:
            print('\n')
            print("If you want to talk with him, enter 'talk', if you want to \
move to another street, enter 'next'")  
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    boss_1.talk()
                    print('\n')
                    print('Kill or say a hint?(enter kill/hint)')
                    com = ''
                    while com not in ('kill', 'hint'):
                        com = input('> ')
                        if com.lower() == 'kill':
                            if 'weapon' in bag:
                                win += 1
                                print('Yoohoo, you won the boss')
                                bag.remove('weapon')
                                current_street = lst_of_streets[2]
                                num += 1
                            elif 'weapon' and 'hint' not in bag:
                                print("Unfortunately, you have been killed, \
        because you don't have any weapon or hint...")
                                dead_status = True
                        if com.lower() == 'hint':
                            print('Unfortunately right now you have no hint')
                        elif com.lower() not in ('kill', 'hint'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[2]
                    num += 1
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")


        elif inhabitant == marshrutka_robber_1:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    marshrutka_robber_1.talk()
                    print('\n')
                    print('Catch him and get some money or move \
    to the next street?(enter "catch" or "next")')
                    inp = ''
                    while inp not in ('catch', 'next'):
                        inp = input('> ')
                        if inp.lower() == 'catch':
                            print('Yooho, now you have some money in your bag')
                            bag.append('money')
                            current_street = lst_of_streets[3]
                            num += 1
                        elif inp.lower() == 'next':
                            current_street = lst_of_streets[3]
                            num += 1
                        elif inp.lower() not in ('catch', 'next'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[3]
                    num += 1

        elif inhabitant == homeless_1:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    homeless_1.talk()
                    print('Do you want to help the homeless?(enter "help" or "next")')
                    comm = ''
                    while comm.lower() not in ('help', 'next'):
                        comm = input('> ')
                        if comm == 'help':
                            if 'money' in bag:
                                word = homeless_1.help(comm, bag)
                                current_street = lst_of_streets[4]
                                num += 1
                            elif 'money' not in bag:
                                print('You have no money to give to a poor man.')
                                current_street = lst_of_streets[4]
                                num += 1
                        elif comm == 'next':
                            current_street = lst_of_streets[4]
                            num += 1
                        elif comm.lower() not in ('help', 'next'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[4]
                    num += 1
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")

        elif inhabitant == cavaler_2:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    cavaler_1.talk()
                    command_2 = ''
                    while command_2 not in ('yes', 'no'):
                        command_2 = input('> ')
                        if command_2.lower() == 'yes':
                            cavaler_2.yes(command_2, bag)
                            current_street = lst_of_streets[5]
                            num += 1
                        elif command_2.lower() == 'no':
                            current_street = lst_of_streets[5]
                            num += 1
                        elif command_2 not in ('yes', 'no'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[5]
                    num += 1
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")

        elif inhabitant == boss_2:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    boss_2.talk()
                    print('\n')
                    print('Kill or say a hint?(enter kill/hint)')
                    com = ''
                    while com.lower() not in ('kill', 'hint'):
                        com = input('> ')
                        if com.lower() == 'kill':
                            if 'weapon' in bag:
                                win += 1
                                print('Yoohoo, you won the boss')
                                bag.remove('weapon')
                                current_street = lst_of_streets[6]
                                num += 1
                                win += 1
                            elif 'weapon' and 'hint' not in bag:
                                print("Unfortunately, you have been killed, \
        because you don't have any weapon or hint...")
                                dead_status = True
                        if com.lower() == 'hint':
                            if 'hint' in bag:
                                print('Say your hint:')
                                inp_t = input('> ')
                                if inp_t == word:
                                    print('Yoohoo, the boss let you down')
                                    bag.remove('hint')
                                    current_street = lst_of_streets[6]
                                    num += 1
                                    win += 1
                                elif inp_t != word:
                                    print('Unfortunately, you did not won\
 the boss, you are killed!')
                                dead_status = True
                        elif com.lower() not in ('kill', 'hint'):
                             print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    current_street = lst_of_streets[6]
                    num += 1

        elif inhabitant == boss_3:
            print('\n')
            print("If you want to talk with him, enter 'talk', \
if you want to move to another street, enter 'next'")
            command = ''
            while command.lower() not in ('talk', 'next'):
                command = input('> ')
                if command.lower() == 'talk':
                    boss_2.talk()
                    print('\n')
                    print('Kill or say a hint?(enter kill/hint)')
                    com = ''
                    while com.lower() not in ('kill', 'hint'):
                        com = input('> ')
                        if com.lower() == 'kill':
                            if 'weapon' in bag:
                                win += 1
                                print('Yoohoo, you won the boss')
                                bag.remove('weapon')
                                win += 1
                            elif 'weapon' and 'hint' not in bag:
                                print("Unfortunately, you have been killed, \
        because you don't have any weapon or hint...")
                                dead_status = True
                        if com.lower() == 'hint':
                            if 'hint' in bag:
                                print('Say your hint:')
                                inp_t = input('> ')
                                if inp_t == word:
                                    print('Yoohoo, the boss let you down')
                                    bag.remove('hint')
                                    win += 1
                                elif inp_t != word:
                                    print('Unfortunately, you did not won \
the boss, you are killed!')
                                    dead_status = True
                        elif com.lower() not in ('kill', 'hint'):
                            print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")
                elif command.lower() == 'next':
                    print('You have no streets left...')
                    if win < 2:
                        print('Unfortunately, you did not won 2 or more bosses... You lost')
                        dead_status = True
                    elif win >= 2:
                        print('You won! You killed 2 or more bosses. My congratulations!')
                        dead_status = True
                elif command.lower() not in ('talk', 'next'):
                    print("""
- - - - - - - - - - - - - 
Invalid input, try again:)
- - - - - - - - - - - - -
""")