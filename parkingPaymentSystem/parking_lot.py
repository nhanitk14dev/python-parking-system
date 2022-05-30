# OOP https://www.geeksforgeeks.org/python-oops-concepts
from array import array
from math import fabs
import re  # https://www.w3schools.com/python/python_regex.asp OR https://www.codespeedy.com/regex-in-python
import json
from os.path import exists
import os.path
from datetime import datetime
from zoneinfo import available_timezones
from common_function import caculate_duration_time_from_parked_to_pickup_time, calculate_parking_cost

# parent class
class Car:
    def __init__(self, car_identity):
        self.car_identity = car_identity

    def validate_car_identity(self):
        """
        Validates if the given value is a valid format like 59C-12345, 01E-00001.
        if not raise ValidationError
        """
        return re.search("^[A-Za-z0-9]{3}[-]{1}[0-9]{4,6}", self.car_identity)

    def find(self):
        try:
            filename = "{}.json".format(self.car_identity)
            file_exists = os.path.exists(filename)
            current_car = None
            if file_exists:
                with open(filename, mode='r') as f:
                    current_car = json.load(f)
                    f.close()
            return current_car

        except Exception as e:
            print("Error: ", e)

    # function to add to JSON
    def write_json(self, new_details, payment):
        try:
            filename = "{}.json".format(self.car_identity)
            file_exists = os.path.exists(filename)
            if file_exists:
                with open(filename, mode='r+') as f:
                    data = json.load(f)

                    # If new detail is pickedup
                    # set another active is false, pickup is false before update
                    if (len(data['details']) and new_details['PickedUp']):
                        for i in data['details']:
                            i['Active'] = False
                            i['PickedUp'] = False
                            i['Parked'] = False

                    # Append new
                    data['details'].append(new_details)
                    data['TotalPayment'] = payment['TotalPayment']
                    data['AvailableCredit'] = payment['AvailableCredit']
                    # Again set the pointer to the beginning, replace new content
                    f.seek(0)
                    json.dump(data, f)
                    f.close()
            else:
                details = []
                details.append(new_details)
                data = {'details': []}
                data['details'] = details
                data['TotalPayment'] = payment['TotalPayment']
                data['AvailableCredit'] = payment['AvailableCredit']

                with open(filename, mode='w') as f:
                    json.dump(data, f)
                    f.close()

            return True
        except Exception as e:
            print("Error: ", e)
            return False

# Child class


class Park(Car):
    def __init__(
        self,
        car_identity,
        arrival_date="",
        arrival_time="",
        frequent_parking_number=""
    ):
        super().__init__(car_identity)
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.frequent_parking_number = frequent_parking_number

    # using None as value of default parameter
    def save_details_as_file(self, is_parked= True, is_active = False, payment = {}):

        # Todo: check car if it's existing, update new data, else new record
        dict_details = {
            'CarIdentity': self.car_identity,
            'ArrivalDate': self.arrival_date,
            'ArrivalTime': self.arrival_time,
            'FrequentParkingNumber': self.frequent_parking_number,
            'Parked': is_parked,
            'PickedUp': not is_parked,
            'Active': is_active
        }

        if payment:
            new_payment = payment
        else:
            new_payment = {
                "TotalPayment": "{:.2f}".format(float(0.00)),
                "AvailableCredit": "{:.2f}".format(float(0.00)),
            }

        return self.write_json(dict_details, new_payment)

    def calculate_display_parking_price(self, car_details):
        try:
            # Todo in the future: Handle get price by day of week. Currently, just calculate in day.
            # Times: from 08:00 - midnight (00:00)
            # Price default: $10.00 per hour (all days are the same)
            # Discount 50% from 17:00 - midnight, 10% for other arrival time.

            price_default = float(10.00)
            # Filter item is active
            if len(car_details['details']):
                active_parked_car = list(filter(lambda item: item['Active'] is True, car_details['details']))
                car_details = active_parked_car[0]

                picked_time = "{} {}".format(car_details['ArrivalDate'], car_details['ArrivalTime'])
                dt = datetime.now()
                current_time = dt.strftime("%Y-%m-%d %H:%M")

                total_hours = caculate_duration_time_from_parked_to_pickup_time(picked_time)
                total_cost = calculate_parking_cost(total_hours)

                return {
                    'car_details': car_details,
                    'picked_time': picked_time,
                    'current_time': current_time,
                    'total_hours': total_hours,
                    'total_cost': total_cost
                }

        except Exception as e:
            print("Error: ", e)


class History(Car):
    def __init__(self, car_identity):
        super().__init__(car_identity)

    def exportHistory(self, car_details):
        
        if len(car_details['details']):
            try:
                filename = "{}.txt".format(self.car_identity)
                with open(filename, mode="w") as f:
                    total_payment = "{:.2f}".format(float(car_details['TotalPayment']))
                    available_credit = "{:.2f}".format(float(car_details['AvailableCredit']))

                    f.write("Total payment: {}\n".format(total_payment))
                    f.write("Available credit: {}\n".format(available_credit))
                    f.write("Parked Dates:\n")
                    for i in car_details['details']:
                        f.write("{} {}\n".format(i['ArrivalDate'], i['ArrivalTime']))
                    f.close()

            except Exception as e:
                print("Erro: ", e)
        else:
            print("No content")

# try:
    # Test Data Step 1.
    # model = Park('84E-12345', '2022-05-29', '14:00', '12345')
    # model.save_details_as_file(True)

    # Test Data Step 2
    # model = Park('84E-12345', '2022-05-29', '14:00', '12345')
    # model.save_details_as_file(False, False)


    # Test calculate parking price
    # park_model = Park('84E-12345')
    # car_details = park_model.find()
    # park_model.calculate_parking_price(car_details)


    # Test Data Step 3
    # car_identity = "84E-12345"
    # car_history_model = History(car_identity)
    # car_history_data = car_history_model.find()
    # car_history_model.exportHistory(car_history_data)

# except Exception as e:
#     print("Erorr: ", e)

# json.loads(jsonstring) #for Json string
# json.loads(fileobject.read()) #for fileobject

# Data example:
# [
#     {
#         "CarIdentity": "84E-12345",
#         "ArrivalDate": "2022-05-05",
#         "ArrivalTime": "13:01",
#         "FrequentParkingNumber": "111111111",
#         "park": 0,
#         "pickup": 0
#     },
#     {
#         "CarIdentity": "84E-12345",
#         "ArrivalDate": "2022-05-05",
#         "ArrivalTime": "13:03",
#         "FrequentParkingNumber": "111111111",
#         "park": 0,
#         "pickup": 0
#     }
# ]
