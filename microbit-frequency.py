from microbit import *

uart.init(baudrate=9600,tx=pin8,rx=pin12)


while True:
    if uart.any():
      message = uart.read()
      display.scroll(message)
    else:
      sleep(20)
    
    if button_a.is_pressed():
        uart.write('read')
        sleep(50)
        
    if button_b.is_pressed():
        uart.write('F10.0')
        sleep(50)
        uart.write('D050')
