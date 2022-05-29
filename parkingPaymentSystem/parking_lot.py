# OOP https://www.geeksforgeeks.org/python-oops-concepts
from array import array
import re  # https://www.w3schools.com/python/python_regex.asp OR https://www.codespeedy.com/regex-in-python
import json
from os.path import exists
import os.path
from datetime import datetime
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

    def save_details_as_file(self, is_parked: True, is_active: False):

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

        return self.write_json(dict_details)

    def calculate_parking_price(self, car_details):
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

                # Print Bill Information
                bill_info = """
                    --- Bill Detail ---\n
                    Car Identity: {}\n
                    Parked Time: {}\n
                    Picked Up Time: {}\n
                    Total Hours: {}\n
                    Total Cost: {}\n
                """.format(car_details['CarIdentity'], picked_time, current_time, total_hours, total_cost)

                print(bill_info)

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

# try:
    # Test Data Step 1.
    # model = Park('84E-12345', '2022-05-29', '14:00', '12345')
    # model.save_details_as_file(True)

    # Test Data Step 2
    # model = Park('84E-12345', '2022-05-29', '14:00', '12345')
    # model.save_details_as_file(False)


    # Test calculate parking price
    park_model = Park('84E-12345')
    car_details = park_model.find()
    park_model.calculate_parking_price(car_details)


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
