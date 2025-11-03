import bluetooth
import struct
from micropython import const

_UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_UART_TX = (bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_NOTIFY,)
_UART_RX = (bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_WRITE,)

_UART_SERVICE = (_UART_UUID, (_UART_TX, _UART_RX,),)

class BLEPeripheral:
    def __init__(self, ble, name="ESP32"):
        self._ble = ble
        self._ble.active(True)
        self._ble.config(gap_name=name)
        self._ble.irq(self._irq)
        ((self._tx, self._rx,),) = self._ble.gatts_register_services((_UART_SERVICE,))
        #result = self._ble.gatts_register_services((_UART_SERVICE,))<----------- can also be written like this
        self._connections = set()
        self._handler = None
        self._advertise()

    def _irq(self, event, data):
        if event == 1:  # connect
            self._connections.add(data[0])
        elif event == 2:  # disconnect
            self._connections.remove(data[0])
            self._advertise()
        elif event == 3:  # write
            conn, value_handle = data
            if value_handle == self._rx and self._handler:
                self._handler(self._ble.gatts_read(self._rx))

    def on_write(self, handler):
        self._handler = handler

    def _advertise(self, interval_us=500000):
        name = bytes("ESP32_RC_CAR", "utf-8")
        adv = bytearray(b'\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name
        self._ble.gap_advertise(interval_us, adv)
