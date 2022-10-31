## PWM对象构造函数:

```python
machine.PWM(pin)
"""
作用：指定GPIO重新初始化，设置为PWM输出

pin：同GPIO中的PIN用于指定端口使其重新初始化

"""
```

## PWM反初始化函数:

```python
PWM.deinit()

"""

作用：清空初始化，停止PWM输出

"""
```

## 设置PWM频率函数:

```python
PWM.freq([value])

"""
作用：设置PWM波的频率

value: 自动计算分频计数器和Top寄存器的参数，决定了计数器的最大计数值

"""
```

## 设置占空比函数：

```python
PWM.duty_u16([value])

"""
作用：设置占空比

value:设置占空的比例，数值在0~65536之间

"""
```

## 设置高电平时间函数：

```python
PWM.duty_ns([value])

"""
作用：设置高电平持续的时间

value: 设置时间单位为 ns
"""
```

