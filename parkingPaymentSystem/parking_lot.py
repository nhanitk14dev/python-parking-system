# OOP https://www.geeksforgeeks.org/python-oops-concepts
from array import array
from cgi import print_arguments
from operator import le
import re  # https://www.w3schools.com/python/python_regex.asp OR https://www.codespeedy.com/regex-in-python
import json
from os.path import exists
import os.path

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
        except Exception as e:
            print("Error: ", e)

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

        self.write_json(dict_details)


# Test Data
# a = Park('84E-12313', '2022-05-05 13:01', '111111111')
# a.details()
# a.save_details_as_file()
# a = Park('84D-11111', '2022-28-05', '14:01', '444412313')
# a.save_details_as_file()

# json.loads(jsonstring) #for Json string
# json.loads(fileobject.read()) #for fileobject

# Data example:
# [
#     {
#         "CarIdentity": "84E-12313",
#         "ArrivalDate": "2022-05-05",
#         "ArrivalTime": "13:01",
#         "FrequentParkingNumber": "111111111",
#         "park": 0,
#         "pickup": 0
#     },
#     {
#         "CarIdentity": "84E-12313",
#         "ArrivalDate": "2022-05-05",
#         "ArrivalTime": "13:01",
#         "FrequentParkingNumber": "111111111",
#         "park": 0,
#         "pickup": 0
#     }
# ]
