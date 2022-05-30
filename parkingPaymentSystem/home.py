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

                parking_entity.save_details_as_file(True, True)
                print('The detail updated succeessfully!')
                startSystem()
            elif input_option == 2:
                # Todo: Check valid format like 59C-12345, 01E-00001.
                car_identity = checkCarIdentityValidate()
                car = Car(car_identity)
                car_details = car.find()
                if car_details is None:
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

                    print("---System calculate and show the parking price---")
                    bill_details = parking_model.calculate_display_parking_price(car_details)

                    if bill_details: 
                        # Print Bill Information
                        bill_info = """
                            --- Bill Detail ---\n
                            Car Identity: {}\n
                            Parked Time: {}\n
                            Picked Up Time: {}\n
                            Total Hours: {}\n
                            Total Cost: {}\n
                        """.format(
                            car_identity, 
                            bill_details['picked_time'], 
                            bill_details['current_time'], 
                            bill_details['total_hours'], 
                            bill_details['total_cost']
                            )

                        print(bill_info)

                        payment_amount = paymentAmountValidate(bill_details['total_cost'])
                        """
                            The exceed amount will be kept for next payment (stored in file)
                            System will update detail including active is false, TotalPayment, AvailableCredit
                        """

                        total_payment = float(car_details['TotalPayment']) + float(bill_details['total_cost'])
                        print(total_payment)
                        available_credit = float(car_details['AvailableCredit']) + (float(payment_amount) - float(bill_details['total_cost']))
                        payment = {
                            "TotalPayment": "{:.2f}".format(total_payment),
                            "AvailableCredit": "{:.2f}".format(available_credit),
                        }

                        parking_model.save_details_as_file(is_parked = False, is_active = False, payment = payment)
                        print('The detail updated succeessfully!')
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


def paymentAmountValidate(total_cost):
    payment_amount = float(input("Payment Amount: "))
    try:
        if isinstance(payment_amount, (int, float)):
            if (payment_amount < float(total_cost)):
                print('Your payment amount must be greater than or equal total cost')
                paymentAmountValidate(total_cost)
            else:
                return payment_amount
        else:
            print('Your payment amount must to be int or float')
            paymentAmountValidate(total_cost)
    except ValueError as e:
        print('Error', e)

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

# Run system
welcome()
startSystem()


#Test data
# paymentAmountValidate('300')