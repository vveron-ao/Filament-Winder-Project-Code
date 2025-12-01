from machine import Pin
from time import sleep_us, sleep

# -------------------------
# PIN DEFINITIONS
# -------------------------
DIR_PIN = 26      # Direction pin
STEP_PIN = 27     # Step pin
EN_PIN = 28       # Enable pin (active LOW)

# -------------------------
# INITIALIZATION
# -------------------------
dir_pin = Pin(DIR_PIN, Pin.OUT)
step_pin = Pin(STEP_PIN, Pin.OUT)
en_pin = Pin(EN_PIN, Pin.OUT)

# Enable driver (0 = active)
en_pin.value(0)

# Set direction
dir_pin.value(1)  # 1 = CW, 0 = CCW

# -------------------------
# MOTOR PARAMETERS
# -------------------------
STEPS_PER_REV = 200      # NEMA 23 = 200 steps in full-step mode
STEP_DELAY_US = 1000     # Delay between steps (1000 µs = 1 kHz)

# -------------------------
# ROTATE ONE REVOLUTION
# -------------------------
for _ in range(STEPS_PER_REV):
    step_pin.value(1)
    sleep_us(5)         # DRV8825 minimum step pulse width
    step_pin.value(0)
    sleep_us(STEP_DELAY_US)

# Disable driver after movement (optional)
en_pin.value(1)

print("1 Revolution Complete!")


#### FOR TESTING THE LED & CONFIGURATION OF MICROCONTROLLER ####
# from machine import Pin
# import time

# led = Pin("LED", Pin.OUT)

# while True:
#     led.on()      # Turn LED on
#     time.sleep(1)
#     led.off()     # Turn LED off
#     time.sleep(1)