## Pin :对象构造函数:

```python
machine.Pin(id,mode=None,pull=None,value)	

"""

作用：初始化GPIO口

id : GPIO编号,数值为0-29,如使用GPIO13则此处填写13;

mode : 模式,可选None、Pin.IlN(O)、Pin.OUT(1)、Pin.OPEN_DRAIN(2);

pull : 使用内部上下拉电阻,仅在输入模式下有效，可选None、Pin.PULL_UP(1)、Pin.PULL_DOWN(2);

value : 输出或开漏模式下端口值,0为低(off)、1为高(on);

"""
```

## 重新初始化GPIO口函数:

```python
Pin.init(mode=None, pull=None)

"""
作用：重新初始化GPIO口

mode:模式,可选None、Pin.IlN(O)、Pin.OUT(1)、Pin.OPEN_DRAIN(2);

pull:使用内部上下拉电阻,仅在输入模式下有效,可选None(0)、Pin.PULL_UP(1)、Pin.PULL_DOWN(2);

"""
```

## 获取GPIO口操作函数:

```python
Pin.value([x])

"""
作用：

不填写参数的情况下返回GPIO端口数值，

在填写参数的情况下将参数写入GPIO端口中,参数可为0或者l;

"""
```

## 翻转GPIO口数值函数:

```python
Pin.toggle()

"""

作用：输出或者开漏模式下将端口设置翻转

"""
```

## GPIO口操作函数:

```python
Pin.low()
"""
作用：输出或开漏模式下将端口设置为低(0);
"""
Pin.off()
"""
作用：输出或开漏模式下将端口设置为低(0);
"""
Pin.high()
"""
作用：输出或开漏模式下将端口设置为高(1);
"""
Pin.on()
"""
作用：输出或开漏模式下将端口设置为高(1);
"""
```

## 设置外部中断函数:



```python
Pin.irq(handler=None,trigger=(Pin.IlRQ_FALLING | Pin.IRQ_RISING))
"""
作用：将GPIO口设置为外部中断输入

handler:中断触发回调函数;

trigger:中断触发条件,设置为边缘触发或者电平触发。

"""
```

