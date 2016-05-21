from ubidots import ApiClient
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
        # Get the latest value.
        temp = tempVar.get_values(1)
        print "Got temperature %.1f at %s" % (temp[0]['value'], temp[0]['created_at'])

        time.sleep(5)
    except ValueError:
        print "Value not sent"
