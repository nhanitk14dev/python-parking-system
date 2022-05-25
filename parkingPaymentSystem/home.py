from parking_lot import Car, Park
from datetime import datetime

def welcome():
    print("""Welcome to Console parking payment system""")

def startSystem():
    try:
        input_option = int(input("""
        Please choose an option:
           1. Park (in)
           2. Pickup (out)
           3. History
           """))

        if not isinstance(input_option, int):
            raise ValueError("Not a positive number")
        else:
            if input_option == 1:
                # Todo import Park class
                dt = datetime.now()
                dt_format = dt.strftime("%Y-%m-%d, %H:%M:%S")
                arrival_time = input("The arrival time: {}".format(dt_format)) or dt_format

                # Todo: Check valid format like 59C-12345, 01E-00001.
                car_identity = input("Car identity: ")
                car = Car(car_identity)
                isValid = car.validate_car_identity()

                if isValid is None:
                    print("Your car identity is not format correctly! Please re-input again")
                    car_identity = input("Car identity: ")

                frequent_parking_number = int(input("The frequent parking number(optional): "))
                parking_entity = Park(car_identity, arrival_time, frequent_parking_number)
                saved_park = parking_entity.save_details_as_file()

                # Finished ! go to main menu
                startSystem()

            elif input_option == 2:
                input("The frequent parking number(optional): ")
            elif input_option == 3:
                input("The frequent parking number(optional): ")
            else:
                print("Your option is invalid, please try again.")
                typeAgain()
    except Exception as e:
        print("Error:", e) # This option show only for dev
        print("Oops! That was no valid number. Try again...")
        typeAgain()

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

welcome()
startSystem()