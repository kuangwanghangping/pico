from machine import SoftI2C,Pin
from ssd1306 import SSD1306_I2C
i2c = SoftI2C(scl = Pin(0),sda = Pin(1))
oled = SSD1306_I2C(128,64,i2c)
oled.text("lenglang.xyz",0,0)#(想要显示的东西，第几行，第几列）
oled.show()