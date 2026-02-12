# Code for controlling a dc motor through a h-bridge
import RPi.GPIO as GPIO

motorPin = 12 # pin for controlling the motor

frequency = 100  # Set the PWM frequency in Hz (adjust as needed)
duty_cycle = 100 # Set the duty cycle (100%)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(motorPin, GPIO.OUT) # motor pin set as output
GPIO.setup(23, GPIO.OUT) # en pin set as output
GPIO.setup(24, GPIO.OUT) # en pin set as output

pwm = GPIO.PWM(motorPin, frequency)

print("Here we go! Press CTRL+C to exit")
try:
    pwm.start(duty_cycle)  # Start PWM with 100% duty cycle (fully on)
    GPIO.output(23, GPIO.HIGH) # enable h-bridge
    GPIO.output(24, GPIO.LOW) # enable h-bridge
    while True: # Loop to keep code running
        pass

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop()     # Stop the PWM
    GPIO.cleanup() # cleanup all GPIO
