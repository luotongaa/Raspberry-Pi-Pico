from machine import PWM,Pin
import utime
s = PWM(Pin(7))
s.freq(50)
#s.duty_u16(4915)  # 4915是90度
#utime.sleep(0.5)
s.duty_u16(5200)  # 8192是180度
#s.duty_u16(6000)
#utime.sleep(0.5)
#s.duty_u16(1638)  # 1638是0度


