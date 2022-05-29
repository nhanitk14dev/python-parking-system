from multiprocessing.sharedctypes import Value
from parking_lot import Car, Park, History
from datetime import datetime


def welcome():
    print("""Welcome to Console Parking Payment System""")


def startSystem():
    try:
        input_option = int(input("""
        Please choose an option:
           1. Park (in)
           2. Pickup (out)
           3. History
           ---Press any key to exit system---
           """))

        if not isinstance(input_option, int):
            raise ValueError("Not a positive number")
        else:
            if input_option == 1:

                # Check valid format like 59C-12345, 01E-00001.
                car_identity = checkCarIdentityValidate()
                frequent_parking_number = int(
                    input("The frequent parking number(optional): ") or 0) 

                dt = datetime.now()
                dt_date = dt.strftime("%Y-%m-%d")
                dt_time = dt.strftime("%H:%M")
                print("The arrival time: {}, {}".format(dt_date, dt_time))
                parking_entity = Park(
                    car_identity,
                    dt_date,
                    dt_time,
                    frequent_parking_number
                )

                parking_entity.save_details_as_file(True)
                print('The detail updated succeessfully!')
                startSystem()
            elif input_option == 2:
                # Todo: Check valid format like 59C-12345, 01E-00001.
                car_identity = checkCarIdentityValidate()
                car = Car(car_identity)
                current_car = car.find()
                if current_car is None:
                    raise ValueError(
                        "Not valid car identity found! Please try again")
                else:
                    # print(current_car)
                    dt = datetime.now()
                    dt_date = dt.strftime("%Y-%m-%d")
                    dt_time = dt.strftime("%H:%M")
                    #frequent_parking_number todo: get existing value
                    parking_model = Park(
                        car_identity,
                        dt_date,
                        dt_time
                    )
                    parking_model.save_details_as_file(False)
                    print('The detail updated succeessfully!')

                    """Sytem calculate and show the parking price"""
                    parking_price_detail = parking_model.calculate_display_parking_price()


                startSystem()
            elif input_option == 3:
                # Todo: Check valid format like 59C-12345, 01E-00001.
                car_identity = checkCarIdentityValidate()
                car_history_model = History(car_identity)
                car_history_data = car_history_model.find()
                if car_history_data is None:
                    raise ValueError(
                        "Not valid car identity found! Please try again")
                else:
                    car_history_model.exportHistory(car_history_data)
                    print('a file have been exported')
                startSystem()    
            else:
                print("Your option is invalid, please try again.")
                typeAgain()
    except Exception as e:
        print("Error:", e)  # This option show only for dev
        print("Oops! That was no valid number. Try again...")
        typeAgain()

# Todo: create new common fucntion to turn back input and check validate too


def checkCarIdentityValidate():
    car_identity = input("Car identity: ")
    car = Car(car_identity)
    isValid = car.validate_car_identity()
    if isValid is None:
        print("Oops! Your car identity is not format correctly!")
        option = input("""Do you want to try again?
                        Please type Y for YES or N for No.
                    """)

        if option.upper() == 'Y':
            checkCarIdentityValidate()
        else:
            startSystem()
    else:
        return car_identity


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
