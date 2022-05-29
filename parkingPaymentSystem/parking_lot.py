# OOP https://www.geeksforgeeks.org/python-oops-concepts
from array import array
from cgi import print_arguments
from operator import le
import re  # https://www.w3schools.com/python/python_regex.asp OR https://www.codespeedy.com/regex-in-python
import json
from os.path import exists
import os.path
from zoneinfo import available_timezones

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
    def write_json(self, new_data):
        try:
            filename = "{}.json".format(self.car_identity)
            file_exists = os.path.exists(filename)
            if file_exists:
                with open(filename, mode='r+') as f:
                    data = json.load(f)
                    data['details'].append(new_data)
                    # Again set the pointer to the beginning, replace new content
                    f.seek(0)
                    json.dump(data, f)
                    f.close()
            else:
                details = []
                details.append(new_data)
                data = {'details': []}
                data['details'] = details

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

    def save_details_as_file(self):

        # Todo: check car if it's existing, update new data, else new record
        dict_details = {
            'CarIdentity': self.car_identity,
            'ArrivalDate': self.arrival_date,
            'ArrivalTime': self.arrival_time,
            'FrequentParkingNumber': self.frequent_parking_number
        }

        return self.write_json(dict_details)


class History(Car):
    def __init__(self, car_identity):
        super().__init__(car_identity)

    def exportHistory(self, car_details):
        
        if len(car_details['details']):
            try:
                filename = "{}.txt".format(self.car_identity)
                with open(filename, mode="w") as f:
                    total_payment = 0.00
                    formatted_total_payment = "{:.2f}".format(total_payment)

                    available_credit = 0.00
                    formatted_available_credit = "{:.2f}".format(available_credit)

                    f.write("Total payment: {}\n".format(formatted_total_payment))
                    f.write("Available credit: {}\n".format(formatted_available_credit))
                    f.write("Parked Date:\n")
                    for i in car_details['details']:
                        f.write("{}-{}\n".format(i['ArrivalDate'], i['ArrivalTime']))
                    f.close()

            except Exception as e:
                print("Erro: ", e)
        else:
            print("No content")


    
# Test Data Step 1.
# a = Park('84E-12345', '2022-05-05 13:01', '111111111')
# a.details()
# a.save_details_as_file()

# Test Data Step 2:
# a = Park('84E-12345', '2022-28-05', '14:01', '444412313')
# a.save_details_as_file()

# Test Data Step 3:
# car_identity = "84E-12345"
# car_history_model = History(car_identity)
# car_history_data = car_history_model.find()
# car_history_model.exportHistory(car_history_data)

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
