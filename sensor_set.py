from ubidots import ApiClient
import random
import time

# Create an ApiClient object
api = ApiClient(token='BQVCK7vEK1t59qPNFGVgCdyZ8HRogc')

# Get a Ubidots Variable
try:
    tempVar = api.get_variable("573fb3c576254202abeb4d89")
except ValueError:
    print "It is not possible to obtain the variable"

while(1):
    try:
        # Random generate the temperature.
        v = random.randint(10, 30)
        tempVar.save_value({'value': v})
        print "Sent value %d to server" % v

        time.sleep(5)
    except ValueError:
        print "Value not sent"
