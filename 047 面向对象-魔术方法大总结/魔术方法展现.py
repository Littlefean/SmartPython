# -*- encoding: utf-8 -*-
"""
PyCharm 魔术方法展现
2022年07月01日
by littlefean
"""
from typing import *


def main():
    with open("魔术方法.py", encoding="utf-8") as f:
        arr = f.readlines()
    content = [line.strip() for line in arr if "def __" in line]
    print("\n".join(content))

    """
    
    调用相关
    def __init__(self):
    def __call__(self, *args, **kwargs):
    def __getitem__(self, item):
    def __int__(self):
    
    字符化
    def __repr__(self):
    def __str__(self):
    
    迭代相关
    def __next__(self):
    def __iter__(self):
    
    内置函数调用触发
    def __len__(self):
    def __hash__(self):
    def __abs__(self):
    def __copy__(self):
    def __getattr__(self, item):
    def __format__(self, format_spec):
    def __deepcopy__(self, memodict=None):
    def __round__(self, n=None):
    def __pow__(self, power, modulo=None):

    def __sizeof__(self):
    
    对象进行特殊运算
    def __getattribute__(self, item):
    
    转化成其他类型
    def __oct__(self):
    def __hex__(self):
    def __bool__(self):
    def __bytes__(self):
    def __float__(self):
    def __complex__(self):
    
    对象和橘色关键字组合触发
    def __contains__(self, item):
    def __del__(self):
    
    def __exit__(self, exc_type, exc_val, exc_tb):
    def __enter__(self):
    
    运算相关
    def __matmul__(self, other):
    def __neg__(self):
    def __pos__(self):
    def __eq__(self, other):
    def __le__(self, other):
    def __lt__(self, other):
    def __mod__(self, other):
    def __mul__(self, other):
    def __ne__(self, other):
    def __or__(self, other):
    def __ror__(self, other):
    def __sub__(self, other):
    def __xor__(self, other):
    def __idiv__(self, other):
    def __iadd__(self, other):
    def __iand__(self, other):
    def __imod__(self, other):
    def __imul__(self, other):
    def __ipow__(self, other):
    def __isub__(self, other):
    def __ixor__(self, other):
    def __radd__(self, other):
    def __rand__(self, other):
    def __rdiv__(self, other):
    def __rmod__(self, other):
    def __rmul__(self, other):
    def __rpow__(self, other):
    def __rsub__(self, other):
    def __rxor__(self, other):
    def __divmod__(self, other):
    def __lshift__(self, other):
    def __add__(self, other):
    def __and__(self, other):
    def __cmp__(self, other):
    def __ge__(self, other):
    def __gt__(self, other):
    def __ior__(self, other):
    def __coerce__(self, other):
    def __rshift__(self, other):
    def __ilshift__(self, other):
    def __imatmul__(self, other):
    def __irshift__(self, other):
    def __rdivmod__(self, other):
    def __rlshift__(self, other):
    def __rmatmul__(self, other):
    def __rrshift__(self, other):
    def __truediv__(self, other):
    def __floordiv__(self, other):
    def __ifloordiv__(self, other):
    def __itruediv__(self, other):
    def __rfloordiv__(self, other):
    def __rtruediv__(self, other):
    
    
    
    def __index__(self):
    def __ceil__(self):
    
    def __long__(self):
    def __aiter__(self):
    def __anext__(self):
    def __await__(self):
    
    def __floor__(self):
    def __trunc__(self):
    def __invert__(self):
    def __aenter__(self):
    def __fspath__(self):
    def __reduce__(self):
    def __unicode__(self):
    def __getnewargs__(self):
    def __getstate__(self):
    def __reversed__(self):
    def __getinitargs__(self):
    def __delattr__(self, item):
    def __delitem__(self, key):
    
    
    
    
    def __missing__(self, key):
    def __delslice__(self, i, j):
    def __instancecheck__(self, instance):
    
    
    def __get__(self, instance, owner):
    def __set__(self, instance, value):
    def __delete__(self, instance):
    
    def __new__(cls, *args, **kwargs):
    
    
    def __setstate__(self, state):
    def __subclasscheck__(self, subclass):
    def __prepare__(cls, name, bases):
    def __setattr__(self, key, value):
    def __setitem__(self, key, value):
    def __class_getitem__(cls, item):
    def __init_subclass__(cls, **kwargs):
    def __mro_entries__(self, bases):
    def __reduce_ex__(self, protocol):
    def __dir__(self) -> Iterable[str]:
    def __setslice__(self, i, j, sequence):
    def __set_name__(self, owner, name):
    def __class__(self: __rpow__) -> Type[__rpow__]:
    def __aexit__(self, exc_type, exc_val, exc_tb):

    """

    class A:
        def __getattr__(self, item):
            print(item)
            ...

    a = A()
    getattr(a, "abab")
    a.b = 15
    setattr(a, "ss", 15)
    print(a.ss)


    return None


if __name__ == "__main__":
    main()
