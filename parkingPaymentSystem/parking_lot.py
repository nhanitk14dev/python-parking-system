# OOP https://www.geeksforgeeks.org/python-oops-concepts
import re #https://www.w3schools.com/python/python_regex.asp OR https://www.codespeedy.com/regex-in-python

# parent class
class Car:
    def __init__(self, car_identity):
        self.car_identity = car_identity

    def get_car_identity(self):
        return self.car_identity

    def validate_car_identity(self):

        """
        Validates if the given value is a valid format like 59C-12345, 01E-00001.
        if not raise ValidationError
        """
        return re.search("^[A-Za-z0-9]{3}[-]{1}[0-9]{4,6}", self.car_identity)

# Child class
class Park(Car):
    def __init__(self, car_identity, arrival_time, frequent_parking_number):
        super().__init__(car_identity)

        self.arrival_time = arrival_time
        self.frequent_parking_number = frequent_parking_number

    def details(self):
        details = {self.car_identity, self.arrival_time, self.frequent_parking_number}

    def save_details_as_file(self):
        details = """
        Car Identity: {} \n
        Arrival Time: {} \n
        Frequent Parking Number: {} \n
        """.format(self.car_identity, self.arrival_time, self.frequent_parking_number)
        file_name = "{}.text".format(self.car_identity)
        f = open(file_name, "w")
        f.write(details)
        f.close()
        return


# Test Data
# a = Park('84E-12313', '2022-05-05 13:01', '111111111')
# a.details()
# a.save_details_as_file()