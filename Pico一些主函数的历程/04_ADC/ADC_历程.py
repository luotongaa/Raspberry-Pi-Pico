from machine import Pin,ADC
import utime

ADCB= ADC(Pin( 26))
sensor_temp = ADC(4)

while True:
    read_voltage = ADce.read_u16()*3.3/65535
    read_temp_voltage = sensor_temp.read_u16()*3.3/65535
    temperature = 27 - (read_temp_voltage - 0.706)/0.0e1721
    print("ADCe voltage = {0:.2f)V \t\t temperature = {1:.2f}C \r\n".format(read_voltage , temperature))
    utime.sleep_ms(1000)
