## UART对象构造函数：

```python
machine.UART(id,baudrate,bits=8,parity=None,stop=1,tx=None,rx=None)

"""

作用：初始化对应通道和引脚

id: 使用 UART 通道，可为 0 或者 1

baudrate: 波特率参数

bits: 数据位长度

parity: 奇偶校验位

stop: 停止位

tx: TXD引脚，应为Pin对象

rx: RXD引脚，应为Pin对象

"""
```

## 检测缓冲区数据函数：

```python
UART.any()

"""

any函数，用于检测当前接收缓冲区是否有数据，接收缓冲区有数据就返回1，否则返回0

"""
```

## 读取字符串函数：

```python
UART.read([nbytes])

"""

作用：read函数，用于字符串的读取

nbytes: 指定最多读取字节，可以不填，那样会尽可能多的读取数据

"""
```

## 读取一行函数：

```python
UART.readline()

"""

作用：读取一行，一换行符作为结束标志

"""
```

## 字符串存入指定的缓存函数：

```python
UART.readinto(buf,[nbytes])

"""
	
作用：将读取的字符串存入指定缓存

buf: 用于指定缓存

nbytes: 指定最多读取字节，可以不填，那样会尽可能多的读取数据

"""
```

## 字符串发送函数：

```python
UART.write(buf)

"""

作用：用于发送字符串，返回值是发送的字节数

"""
```

## 总线停止发送函数：

```python
UART.sendbreak()

"""

作用：在总线上发送停止信号

"""
```

