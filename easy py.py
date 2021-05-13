Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('hello')
hello
>>> print("hello")
hello
>>> print(''' hello
hello
world''')
 hello
hello
world
>>> 
================================ RESTART: Shell ================================
>>> print('\'hello\'')
'hello'
>>> print('\\hello\\')
\hello\
>>> 
================================ RESTART: Shell ================================
>>> print('abc\nxyz')
abc
xyz
>>> print('hello\nIm\npython\nand\nim\nhappy')
hello
Im
python
and
im
happy
>>> 
================================ RESTART: Shell ================================
>>> print('abc\txyz')
abc	xyz
>>> print('hello\tIm\tKamado\tTanjiro')
hello	Im	Kamado	Tanjiro
>>> 