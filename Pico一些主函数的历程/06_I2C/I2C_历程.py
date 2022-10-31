from machine import I2C,Pin

i2c = I2C(id=1,scl=Pin(7 ),sda=Pin(6) ,freq=100_000)

addr_list = i2c.scan()

if len(addr_list) == 1:
    who = i2c.readfrom_mem( addr_list[e],ox00,1)
    # Identify ICM20948
    if who[0] == exEA:
        print( "Just a ICM20948 connected")
    else:
        print( "Have a device connected but it is not ICM20948")
elif len( addr_list) == 0:
    print("Nothing connected" )
else:
    print( "More than one device is connected" )
