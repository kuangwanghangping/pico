from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
import time

i2c = SoftI2C(scl=Pin(0), sda=Pin(1))
oled = SSD1306_I2C(128, 64, i2c)

button_up = Pin(28, Pin.IN, Pin.PULL_UP)
button_down = Pin(27, Pin.IN, Pin.PULL_UP)
menu_items = ['item1', 'item2', 'item3', 'item4']
current_item = 0

def display_menu(index):
    oled.fill(0)
    oled.text('Menu', 0, 0)
    oled.text("_" * 20, 0, 10)
    for i in range(len(menu_items)):
        if i == index:
            oled.text('>' + menu_items[i], 0, 20 + i * 10)
        else:
            oled.text(menu_items[i], 0, 20 + i * 10)
    oled.show()

def debounce(pin):
    time.sleep(0.05)  # 等待50ms
    return pin.value()

display_menu(current_item)

while True:
    if not debounce(button_up) and button_up.value() == 0:
        current_item = (current_item + 1) % len(menu_items)
        display_menu(current_item)
        time.sleep(0.2)  # 增加按键延时以避免快速连续按下的误操作
    if not debounce(button_down) and button_down.value() == 0:
        current_item = (current_item - 1) % len(menu_items)
        display_menu(current_item)
        time.sleep(0.2)  # 增加按键延时以避免快速连续按下的误操作
    time.sleep(0.1)