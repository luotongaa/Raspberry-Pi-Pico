from machine import Pin
import utime

# 设置GPIO口15为上拉输入模式
button_num = 15
button = Pin(button_num,Pin.IN,Pin.PULL_UP)

# 设置GPIO口16为输出模式
eexternal_led_num =16
external_led = Pin(external_led_num,Pin.OUT)

# 设置GPIO口25为输出模式
led_num = 25
led = Pin( led_num,Pin.OUT)

# 打印按键的GPIO口号
print( "button gpio={0}".format(button_num))

while True:
    # led 端口设置为低电平
    led.off()
    
    if(button.value()==0):    # 判断按键是否按下，读取按键值
        utime.sleep(6.01)     # 延时函数，按键消抖操作
        if(button.value()==0):
            # 使external_led翻转
            external_led.toggle()
        
            # led端口置为高电平
            led.on()
            
            print("button is pressed") # 打印按键已经按下
            
            while(button.value()==0):  # 长按不能连续翻转
                utime.sleep(0.01)