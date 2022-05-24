def welcome():
    print("""Welcome to Console parking payment system""")

def typeAgain():
    type_again = input("""
        Do you want to choose again?
        Please type Y for YES or N for No.
    """)

    if type_again.upper() == 'Y':
        startSystem()
    elif type_again.upper() == 'N':
        print('See you later.')
        quit()
    else:
        typeAgain()

def startSystem():
    input_option = int(input("""
                            Please choose an option:
                               1. Park (in)
                               2. Pickup (out)
                               3. History
                               """))

    #todo check validate only input number
    if isinstance(input_option, int):
        if input_option == 1:
            #todo: get new function to to next step
            print("Customer choose option number {}".format(input_option))
        elif input_option == 2:
            print("Customer choose option number {}".format(input_option))
        elif input_option == 3:
                print("Customer choose option number {}".format(input_option))
        else:
            print("Your option is invalid, please try again.")
            typeAgain()
    else:
        print("Your option is invalid, please try again.")
        typeAgain()

welcome()
startSystem()