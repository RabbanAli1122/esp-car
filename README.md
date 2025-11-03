# 🚗 ESP32 Bluetooth RC Car

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)  
[![MicroPython](https://img.shields.io/badge/MicroPython-1.20+-blue.svg)](https://micropython.org/)  
[![ESP32](https://img.shields.io/badge/ESP32-Compatible-red.svg)](https://www.espressif.com/en/products/socs/esp32)  
[![Bluetooth](https://img.shields.io/badge/Bluetooth-BLE-blue.svg)](https://www.bluetooth.com/)
[![HTML](https://img.shields.io/badge/HTML5-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)  
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  

A wireless RC car controlled via **Bluetooth Low Energy (BLE)** using an **ESP32** microcontroller. The project features a responsive **web-based remote control interface** that works on any smartphone or tablet, enabling real-time control of drive and steering motors with simultaneous command support.

> Perfect for learning IoT, embedded systems, BLE communication, and motor control with ESP32 and MicroPython!

## ✨ Features

- **Bluetooth Low Energy (BLE)** communication for wireless control
- **Dual motor control** - independent drive and steering motors
- **Simultaneous commands** - turn while moving forward/backward
- **PWM speed control** for smooth motor operation
- **Responsive web interface** optimized for mobile devices
- **Landscape mode UI** with intuitive touch controls
- **Real-time state management** for precise motor control
- **Auto-reconnect capability** with connection status indicators

## Project captures:
![WhatsApp Image 2025-11-03 at 23 24 21](https://github.com/user-attachments/assets/b80c65cc-b2dd-4c7e-9216-ad892fb2162d)

![WhatsApp Image 2025-11-03 at 23 24 21 (1)](https://github.com/user-attachments/assets/01ec5ef9-33f1-4c42-a47b-131527c37bb1)

![WhatsApp Image 2025-11-03 at 23 24 20](https://github.com/user-attachments/assets/38668fbd-8a67-4ae7-a3ef-f92fdfde657d)

![WhatsApp Image 2025-11-03 at 23 24 20 (1)](https://github.com/user-attachments/assets/7f974a31-2f7e-44ed-bb0c-c8faaf62ce54)


## Live Demo

[Add your demo video/GIF here]

## 🛠️ Technologies Used

### Hardware
- **ESP32** development board
- **L298N** or similar dual H-bridge motor driver
- **DC motors** (2x) - one for drive, one for steering
- **Power supply** (7.4V Li-Po battery recommended)
- **RC car chassis** with wheels

### Software
- **MicroPython** - firmware for ESP32
- **Bluetooth Low Energy (BLE)** - wireless communication protocol
- **HTML5, CSS3, JavaScript** - web-based remote control
- **Web Bluetooth API** - browser-to-device communication

## 🔌 Hardware Connections

### Motor Driver Wiring (L298N)

| ESP32 Pin | L298N Pin | Function |
|-----------|-----------|----------|
| GPIO 27   | ENA       | Steering PWM |
| GPIO 25   | IN1       | Steering Direction 1 |
| GPIO 26   | IN2       | Steering Direction 2 |
| GPIO 13   | ENB       | Drive PWM |
| GPIO 33   | IN3       | Drive Direction 1 |
| GPIO 32   | IN4       | Drive Direction 2 |
| GND       | GND       | Common Ground |

**Note:** Connect motor driver VCC to battery positive terminal (7.4V) and motors to OUT1/OUT2 (steering) and OUT3/OUT4 (drive).

## 🚀 Getting Started

### 📋 Prerequisites

1. **ESP32 board** with MicroPython firmware installed
2. **USB cable** for programming
3. **Motor driver module** (L298N or equivalent)
4. **DC motors** and RC car chassis
5. **Python 3** installed on your computer
6. **Thonny IDE** or **ampy** for file transfer

### 🔧 Install MicroPython on ESP32

If you haven't installed MicroPython yet:

```bash
# Download MicroPython firmware from micropython.org
# Flash using esptool
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-micropython.bin
```

### 📁 Upload Project Files

1. **Clone the repository:**
```bash
git clone https://github.com/RabbanAli1122/esp-car.git
cd esp-car
```

2. **Upload files to ESP32** using Thonny or ampy:

```bash
# Using ampy
pip install adafruit-ampy
ampy --port /dev/ttyUSB0 put boot.py
ampy --port /dev/ttyUSB0 put main.py
ampy --port /dev/ttyUSB0 put ble_simple_peripheral.py
ampy --port /dev/ttyUSB0 put motor_functions.py
```

Or use **Thonny IDE**:
- Open each file in Thonny
- Save to device (MicroPython device)

3. **Reset the ESP32** - the car will start advertising as `ESP32_RC_CAR`

### 📱 Connect and Control

1. Open `remote(webapp).html` in a **BLE-compatible browser**:
   - Chrome (Android/Desktop)
   - Edge (Desktop)
   - Safari (iOS 16+)

2. **Rotate device to landscape mode** (mobile)

3. Click **CONNECT** button

4. Select **ESP32_RC_CAR** from the device list

5. Control the car using touch buttons:
   - **Forward/Reverse** - vertical controls (drive motor)
   - **Left/Right** - horizontal controls (steering motor)

## 🎮 Control Commands

The car supports the following BLE commands:

| Command  | Action |
|----------|--------|
| `forward` | Drive motor forward |
| `reverse` | Drive motor backward |
| `left` | Steer left |
| `right` | Steer right |
| `stop` | Stop all motors and center steering |

**Commands can be combined!** Send `forward` then `left` to turn while moving.

## 📂 Project Structure

```
esp-car/
│
├── boot.py                      # Boot configuration (runs on startup)
├── main.py                      # Main program with BLE and motor control
├── ble_simple_peripheral.py     # BLE UART service implementation
├── motor_functions.py           # Motor control functions (optional/standalone)
├── remote(webapp).html          # Web-based remote control interface
└── README.md                    # This file
```

## 🔍 How It Works

### 1. ESP32 Side (MicroPython)

- **main.py** initializes BLE peripheral with name "ESP32_RC_CAR"
- Creates UART service with Nordic UART UUIDs
- Sets up motor control with PWM for speed regulation
- Maintains independent state for drive and steering
- Processes incoming BLE commands and updates motors accordingly

### 2. Web Remote (HTML/JavaScript)

- Uses **Web Bluetooth API** to scan and connect to ESP32
- Sends commands via BLE UART characteristic
- Implements touch-friendly UI with visual feedback
- Maintains connection state with auto-stop intervals
- Supports simultaneous drive and steer commands

### 3. Motor Control Logic

```python
# Independent state management
drive_state = "stop"    # forward, reverse, or stop
steer_state = "center"  # left, right, or center

# Motors update based on current states
# This allows combining forward+left, reverse+right, etc.
```

## ⚙️ Customization

### Adjust Motor Speed

Edit PWM duty cycle values in `main.py`:

```python
# Drive motor speed (0-1023)
enb.duty(800)  # Change this value (default: 800)

# Steering motor speed (0-1023)
ena.duty(1000)  # Change this value (default: 1000)
```

### Change BLE Device Name

In `ble_simple_peripheral.py`:

```python
name = bytes("ESP32_RC_CAR", "utf-8")  # Change to your preferred name
```

### Modify Pin Assignments

Update pin numbers in `main.py` according to your wiring:

```python
ena = PWM(Pin(27), freq=1000)  # Steering PWM
in1 = Pin(25, Pin.OUT)         # Steering IN1
# ... etc
```

## 🐛 Troubleshooting

### ESP32 not advertising
- Check if MicroPython is properly installed
- Verify `main.py` runs without errors using REPL
- Reset the board (press EN button)

### Motors not responding
- Verify motor driver connections and power supply
- Check if motor driver has sufficient voltage (typically 7-12V)
- Test motors directly with motor_functions.py

### Cannot connect from browser
- Ensure browser supports Web Bluetooth (Chrome/Edge/Safari 16+)
- Check if Bluetooth is enabled on your device
- Try refreshing the page and reconnecting

### Connection drops frequently
- Keep device within 10 meters of ESP32
- Ensure stable power supply to ESP32
- Avoid interference from other 2.4GHz devices

## 🧠 Lessons Learned

### ESP32 & MicroPython
1. How to code **ESP32** with MicroPython firmware
2. Understanding **UART (Universal Asynchronous Receiver/Transmitter)** protocol
3. Working with **serial buses** and communication protocols
4. Implemented **Bluetooth Low Energy (BLE)** on ESP32
5. Understanding **SSID** (Service Set ID) for wireless networks
6. Learning **RSID** (Received Signal ID) concepts
7. Understanding ESP32's **antenna** and RF capabilities

### Wireless Communication
8. **EM waves** fundamentals for wireless communication
9. **RF waves** - transfer and reception principles
10. Understanding **GPIO** (General Purpose Input/Output) pins
11. Orientation and functioning of **antennas**
12. **Reflection of RF waves** and signal propagation
13. Why **2.4MHz and other frequencies** are used in wireless communication
14. Understanding **bandwidth** and frequency variation
15. **Standing waves** - relation between forward and backward waves
16. **Relation of antenna length with RF** wavelength
17. Direction of **EMR (Electromagnetic Radiation)**
18. **RF radiates through plastic** materials
19. **Receiving antenna** design and implementation
20. How **limbs in antenna cause reflection** and signal loss

### Hardware & Electronics
21. **ASK (Amplitude Shift Keying)** and **OOK (On-Off Keying)** modulation techniques
22. Understanding **station interface** and access point concepts
23. Working with **GND, VIN, 3V3** power pins and voltage levels
24. Understanding **Output and Input** pin configurations
25. **Wiring** ESP32 to motor drivers and peripherals
26. Using **breadboard** for prototyping circuits
27. Implementing **WebREPL** for remote code execution and debugging

### Motor Control & PWM
28. Built a **dual motor control system** with independent states
29. Learned **PWM (Pulse Width Modulation)** for motor speed control
30. **H-bridge driver** usage for bidirectional motor control
31. Implemented **state management** for simultaneous drive and steering commands
32. Understanding motor driver pins (ENA, ENB, IN1-IN4)

### Web Development & BLE
33. Created a **responsive web interface** using Web Bluetooth API
34. Implementing **BLE UART service** with Nordic UART UUIDs
35. Working with **Web Bluetooth API** for browser-device communication
36. Designed **mobile-first UI** with touch-optimized controls
37. Implementing **real-time state management** in JavaScript
38. Understanding BLE **characteristics** and **services**

### Software Architecture
39. Writing modular Python code with separate function files
40. Understanding **boot.py** and **main.py** execution flow in MicroPython
41. Implementing **callback functions** for BLE events
42. **Event-driven programming** for motor control
43. Managing **connection states** and auto-reconnect logic


## 🔮 Future Enhancements

- [ ] Add speed control slider in web interface
- [ ] Implement obstacle detection with ultrasonic sensor
- [ ] Add camera module for FPV (First Person View)
- [ ] Battery level monitoring and low battery alerts
- [ ] Gyroscope-based tilt control mode
- [ ] Multiple control modes (normal, sport, eco)
- [ ] Add LED indicators for status
- [ ] Implement proportional steering control

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

1. [MicroPython](https://micropython.org/) - Python for microcontrollers
2. [ESP32](https://www.espressif.com/) - Powerful IoT microcontroller
3. [Web Bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API) - Browser BLE support
4. Nordic Semiconductor for UART service UUIDs
5. Open-source community for inspiration and tutorials

**Made with ❤️ and ESP32** | Happy Building! 🚗💨
