# -*- coding: utf-8 -*-
'''
try:
    print('try...')
    r = 10 / 5
#    print('result:',r)   
except ZeroDivisionError as e: #出现错误执行except，没有错误不执行，
    print('except:',e)         #
else:    #可以在except后加else，没有错误时跳过except执行else
    print('result',r)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:  #多个except可以处理对应的不同类型的错误
    print('ValueError:',e)
except ZeroDivisionError as e: 
    print('ZeroDivisionError:',e)
else:
    print('no error')
finally:
    print('finally...')
print('END')


#所有错误类型都继承自 BaseException ，他就是class中的父类，父类会捕捉子类的错误
#所以在同时出现子类和父类时子类的except不会执行，只会执行父类的except
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    return r
try:
    foo()
except ValueError as e:  # UnicodeErrror是ValueError的子类，所以捕获不到第二个except
    print('ValueError')
except UnicodeError as e:
    print ('UnicodeError')
'''

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''
'''
#调用堆栈
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)
def main():
    bar('0')
main()
print('END')

Traceback (most recent call last):  -->错误的跟踪信息
  File "C:/Users/69544/Desktop/try.py", line 118, in <module>
    main()  -->调用main（） ，但错误不在这
  File "C:/Users/69544/Desktop/try.py", line 117, in main
    bar('0')  -->接着调用bar（‘0’），但错误不在这
  File "C:/Users/69544/Desktop/try.py", line 115, in bar
    return foo(s)  -->接着调用return foo（s），错误还是没找到
  File "C:/Users/69544/Desktop/try.py", line 113, in foo
    return 10 / int(s)  -->最后到return 10/int（s） ，问题找到并报出
ZeroDivisionError: division by zero
'''


#记录错误，用logging模块
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
#ain()
print('END')


#抛出错误
#自定义错误，  尽量用自带，
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value %s' % s)
    return 10/n
#foo('0')

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise      #??????
bar()

