from datetime import datetime

# System will calculate and display the parking price, round 2 decimal format ex: 50.46
# The price of parking regulation is displayed in the table.
def caculate_duration_time_from_parked_to_pickup_time(parked_time, current_time=None):
    # Time pickup is now.
    # https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
    # https://docs.python.org/3/library/datetime.html#module-datetime

    dt = datetime.now()
    current_time = current_time or dt.strftime("%Y-%m-%d %H:%M")

    time_1 = datetime.strptime(parked_time, "%Y-%m-%d %H:%M")
    time_2 = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    timedelta = time_2 - time_1

    # Calculate the difference between two dates in total seconds
    duration_in_second = timedelta.total_seconds() / (60*60)
    hours = float("{:.2f}".format(duration_in_second))
    return hours

# Cal fee default $10 per hour with discount
def calculate_parking_cost(duration_in_hours):
    # Format number hours, ex: 4,2hours -> 5hour
    fee_default = float(10.00)
    total_cost = float("{:.2f}".format(fee_default*duration_in_hours))
    return total_cost
