import sys

def whydoweneedafunctionforthis():
    if len(sys.argv) > 1:
        print("Hello " + sys.argv[1] + "!")
    else:
        print("Hello World!")
whydoweneedafunctionforthis()