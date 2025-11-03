from machine import Pin, PWM

# --- Pin Setup ---
ena = PWM(Pin(27), freq=1000)  # Motor A PWM (steering)
in1 = Pin(25, Pin.OUT)
in2 = Pin(26, Pin.OUT)

enb = PWM(Pin(13), freq=1000)  # Motor B PWM (drive)
in3 = Pin(33, Pin.OUT)
in4 = Pin(32, Pin.OUT)

# Initialize all pins to 0
in1.value(0)
in2.value(0)
in3.value(0)
in4.value(0)
ena.duty(0)
enb.duty(0)

print("✅ Motors ready")

def forward():
    """Drive forward"""
    in3.value(1)
    in4.value(0)
    enb.duty(800)
    print("Forward")

def reverse():
    """Drive reverse"""
    in3.value(0)
    in4.value(1)
    enb.duty(800)
    print("Reverse")

def left():
    """Steer left"""
    in1.value(1)
    in2.value(0)
    ena.duty(1000)
    print("Left")

def right():
    """Steer right"""
    in1.value(0)
    in2.value(1)
    ena.duty(1000)
    print("Right")

def stop():
    """Stop all"""
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

    print("Stop")

def center():
    in1.value(0)
    in2.value(0)

print("\nCommands: forward(), reverse(), left(), right(), stop()")

