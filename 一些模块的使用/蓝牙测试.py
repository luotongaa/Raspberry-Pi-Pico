import machine
import utime
from machine import Pin,PWM

uart = machine.UART(0, baudrate=9600, tx=machine.Pin(16), rx=machine.Pin(17))
print(uart)

right_eye = PWM(Pin(0))
left_eye = PWM(Pin(1))
RF1 = PWM(Pin(2))
RB1 = PWM(Pin(3))
LF1 = PWM(Pin(4))
LB1 = PWM(Pin(5))
RF2 = PWM(Pin(6))
RB2 = PWM(Pin(7))
LF2 = PWM(Pin(8))
LB2 = PWM(Pin(9))



right_eye.freq(50)
left_eye.freq(50)
RF1.freq(50)
RB1.freq(50)
LF1.freq(50)
LB1.freq(50)
RF2.freq(50)
RB2.freq(50)
LF2.freq(50)
LB2.freq(50)


def up_eye():
    right_eye.duty_u16(3215)  
    left_eye.duty_u16(5215)  
    utime.sleep(0.5)    

def down_eye():
    right_eye.duty_u16(1315)  
    left_eye.duty_u16(7715)  
    utime.sleep(0.5)

def set_down():
    RF2.duty_u16(5200)  
    RB2.duty_u16(8300)   
    LF2.duty_u16(7200)  
    LB2.duty_u16(6000)  

def stant_up():
    RF2.duty_u16(8300)  
    RB2.duty_u16(5200)  
    LF2.duty_u16(6000)  
    LB2.duty_u16(7200)  
def start_init():
    RF1.duty_u16(2215)
    RB1.duty_u16(3315)  
    LF1.duty_u16(4015)
    LB1.duty_u16(3015)

def Go_Frist():
    RF2.duty_u16(8300)
    RB2.duty_u16(6000)  
    LF2.duty_u16(6500)
    LB2.duty_u16(7200)
    RF1.duty_u16(2215)  
    RB1.duty_u16(4315)  
    LF1.duty_u16(3015)
    LB1.duty_u16(3715)
    utime.sleep(0.1)
    RF2.duty_u16(8300)  
    RB2.duty_u16(5200)  
    LF2.duty_u16(6000)  
    LB2.duty_u16(7200)
    
def Go_Scend():
    RF2.duty_u16(7800)
    RB2.duty_u16(5200)
    LF2.duty_u16(6000)
    LB2.duty_u16(6800) 
    RF1.duty_u16(3415)
    RB1.duty_u16(2015)  
    LF1.duty_u16(4015) 
    LB1.duty_u16(2015)
    utime.sleep(0.1)
    RF2.duty_u16(8300)  
    RB2.duty_u16(5200)  
    LF2.duty_u16(6000)  
    LB2.duty_u16(7200)
    
    
stant_up()
start_init()        



while True: 
    Go_Frist()
    utime.sleep(0.5) 
    Go_Scend()
    utime.sleep(0.5) 

#set_down()
"""
while True:
    
    if uart.any():
        
        cmd = uart.readline()
        print(cmd)
    
        if cmd == b'\xfe':            # 眼睛朝下
            stant_up()

        if cmd == b'\xff':            # 眼睛朝上
            set_down()
    
    utime.sleep(0.1)

"""


