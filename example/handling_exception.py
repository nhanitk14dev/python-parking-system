from ctypes import Structure
from xmlrpc.client import Boolean


# Exception handling structure

def handling_sample_1(sample):
    for item in sample:
        try:
            print("Prepare to process item:", item)
            half = item / 2
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            print("Error message:", e)
        else:
            print("Half of the item {}: {}".format(item, half))
        finally:
            print("Calculatation is finished!")
            print("---------------End--------------")

# Raising exception
def handling_sample_2(sample):
    for item in sample:
        try:
            print("Prepare to process item:", item)
            if not isinstance(item, int) or item < 0:
                raise ValueError("Not a positive number!")
            else:
                print("Haft of the item {}: {}".format(item, item/2))
        except Exception as e:
            print(e)
        finally:
            print("Calcualte is finished")

print(handling_sample_2([10]))