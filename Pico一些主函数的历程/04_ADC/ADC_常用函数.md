## ADC对象构造函数

```python
machine.ADC(id)

"""

作用：初始化对应 ADC 通道，可用 GPIO对象，也可为 ADC 通道

使用Pin对象时，指定的GPIO需要支持ADC功能，即GPIO26-29
指定 ADC 通道，通道0-3对应GPIO 26-29 通道数4则是对应内部温度传感器

"""

ADC.read_u16()

"""

作用：读取对应通道的ADC数值
函数返回值并不是直接返回ADC读取的数值，而是经过处理的数值，数值范围：0-65535


"""
```

