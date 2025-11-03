import bluetooth
from machine import Pin, PWM
import time
from ble_simple_peripheral import BLEPeripheral
# Motor setup
ena = PWM(Pin(27), freq=1000)
in1 = Pin(25, Pin.OUT)
in2 = Pin(26, Pin.OUT)
enb = PWM(Pin(13), freq=1000)
in3 = Pin(33, Pin.OUT)
in4 = Pin(32, Pin.OUT)
# Track current state of each motor independently
drive_state = "stop"  # forward, reverse, or stop
steer_state = "center"  # left, right, or center
def update_motors():
    """Update motor states based on current drive and steer commands"""
    # Handle drive motor (forward/reverse)
    if drive_state == "forward":
        in3.value(1)
        in4.value(0)
        enb.duty(800)
    elif drive_state == "reverse":
        in3.value(0)
        in4.value(1)
        enb.duty(800)
    else:  # stop
        in3.value(0)
        in4.value(0)
    # Handle steering motor (left/right)
    if steer_state == "left":
        in1.value(1)
        in2.value(0)
        ena.duty(1000)
    elif steer_state == "right":
        in1.value(0)
        in2.value(1)
        ena.duty(1000)
    else:  # center
        in1.value(0)
        in2.value(0)
    print(f"State: Drive={drive_state}, Steer={steer_state}")
def forward():
    global drive_state
    drive_state = "forward"
    update_motors()
def reverse():
    global drive_state
    drive_state = "reverse"
    update_motors()
def left():
    global steer_state
    steer_state = "left"
    update_motors()
def right():
    global steer_state
    steer_state = "right"
    update_motors()
def stop():
    global drive_state, steer_state
    drive_state = "stop"
    steer_state = "center"
    update_motors()
# BLE Setup
ble = bluetooth.BLE()
p = BLEPeripheral(ble, name="ESP32_RC_CAR")
def on_rx(v):
    cmd = v.decode().strip().lower()
    print("Received:", cmd)
    if cmd == "forward":
        forward()
    elif cmd == "reverse":
        reverse()
    elif cmd == "left":
        left()
    elif cmd == "right":
        right()
    elif cmd == "stop":
        stop()
p.on_write(on_rx)
print("✅ Ready! Now supports simultaneous drive + steer commands!")
print("Example: Send 'forward' then 'left' to turn while moving")