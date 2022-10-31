from machine import UART,Pin
import utime

uart = UART(0, baudrate=115200,tx=Pin(0) , rx=Pin(1))
led = Pin(25,Pin.OUT)

uart.write( "waveshare Uart Test\rln")
uart.write("Please enter character 0 or 1 to switch the LED on and off\r\n")

while True:
    if uart.any( ) == True:
        buf=uart.read(1)
        if buf == b'1':
            led.on()
            print("LED ON")
            uart.write( "LED ON\r\n")
        elif buf == b'0':
            led.off()
            print( "LED OFF")
            uart.write( "LED OFF\r\n")
        else :
            print("please enter character 0 or 1 to switch the LED on and off")
            uart.write("Please enter character 0 or 1 to switch the LED on and off\r\n")
utime. sleep_ms(1)
#machine.reset()
