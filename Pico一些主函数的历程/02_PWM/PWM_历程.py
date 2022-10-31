from machine import Pin,PWM
# 多导入了PWM类
import utime

# 设置PWM口为25 
LED = PWM(Pin(25))

#设置PWM输出频率为 1000Hz
LED.freq(1000)

LED_duty = 0
LED_direction = 1

while True:
    LED_duty += LED_direction
    
    if LED_duty >= 100:
        LED_duty = 100
        LED_direction = -1
    elif LED_duty <= 0:
        LED_duty = 0
        LED_direction = 1
        
    LED.duty_u16(int(LED_duty * 655.36))
    
    if LED_duty%5 == 0:
        print(LED_duty)
        
    utime.sleep(0.01)
