import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import time

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2)

try:
    while True:
        lcd.clear()
        lcd.message("Hello, Raspberry Pi!\nI2C LCD Integration")

        time.sleep(2)  
        for i in range(16 - 2 + 1):
            lcd.move_right()
            time.sleep(0.5)
            
            time.sleep(1)  

except KeyboardInterrupt:
    lcd.clear()
