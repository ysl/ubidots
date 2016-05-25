import RPi.GPIO as GPIO
from ubidots import ApiClient
import time


# Init GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Create an ApiClient object
api = ApiClient(token='BQVCK7vEK1t59qPNFGVgCdyZ8HRogc')

# Get a Ubidots Variable
try:
    stateVar = api.get_variable("573fbb1f7625423b1d1c0523")
except ValueError:
    print "It is not possible to obtain the variable"

while(1):
    try:
        # Get the latest value.
        state = stateVar.get_values(1)
        v = state[0]['value']
        print "Got state %d at %s" % (v, state[0]['created_at'])
        if v == 1:
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)

        time.sleep(5)
    except ValueError:
        print "Value not sent"
    except KeyboardInterrupt:
        print "Clean GPIO"
        GPIO.cleanup()
